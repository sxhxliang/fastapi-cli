from typing import Callable, Optional
from loguru import logger

from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from starlette import requests, status
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.dependencies.database import get_repository
from app.core.config import JWT_TOKEN_PREFIX, JWT_SECRET_KEY
from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from app.resources import strings
from app.services import jwt


class RWAPIKeyHeader(APIKeyHeader):
    def __init__(
        self,
        *,
        name: str = "Authorization",
        scheme_name: str = None,
        auto_error: bool = True
    ) -> None:
        super().__init__(name=name, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(  # noqa: WPS610
        self, request: requests.Request
    ) -> Optional[str]:
       
        try:
            return await super().__call__(request)
        except StarletteHTTPException as original_auth_exc:
            raise HTTPException(
                status_code=original_auth_exc.status_code,
                detail=strings.AUTHENTICATION_REQUIRED,
            )


def get_current_user_authorizer(*, required: bool = True) -> Callable:  # type: ignore
    return _get_current_user if required else _get_current_user_optional


def _get_authorization_header_retriever(
    *, required: bool = True
) -> Callable:  # type: ignore
    return _get_authorization_header if required else _get_authorization_header_optional


def _get_authorization_header(api_key: str = Security(RWAPIKeyHeader())) -> str:
    logger.debug("api_key", api_key)
    try:
        token_prefix, token = api_key.split(" ")
    except ValueError:
        logger.debug(strings.WRONG_TOKEN_PREFIX, "api_key:",api_key)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=strings.WRONG_TOKEN_PREFIX
        )

    if token_prefix != JWT_TOKEN_PREFIX:
        logger.debug(strings.WRONG_TOKEN_PREFIX, "token_prefix:", token_prefix, "api_key:",api_key)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=strings.WRONG_TOKEN_PREFIX
        )

    return token


def _get_authorization_header_optional(
    authorization: Optional[str] = Security(RWAPIKeyHeader(auto_error=False)),
) -> str:
    logger.debug("authorization", authorization)
    if authorization:
        return _get_authorization_header(authorization)

    return ""


async def _get_current_user(
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
    token: str = Depends(_get_authorization_header_retriever()),
) -> User:

    logger.debug("_get_current_user token:", token)
    try:
        username = jwt.get_username_from_token(token, str(JWT_SECRET_KEY))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=strings.MALFORMED_PAYLOAD
        )

    try:
        return await users_repo.get_user_by_username(username=username)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=strings.MALFORMED_PAYLOAD
        )


async def _get_current_user_optional(
    repo: UsersRepository = Depends(get_repository(UsersRepository)),
    token: str = Depends(_get_authorization_header_retriever(required=False)),
) -> Optional[User]:
    print("_get_current_user_optional token:", token)
    if token:
        return await _get_current_user(repo, token)

    return None
