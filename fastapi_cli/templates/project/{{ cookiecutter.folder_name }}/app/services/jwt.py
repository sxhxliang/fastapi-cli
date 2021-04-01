
from typing import Dict
from loguru import logger
from datetime import datetime, timedelta


import jwt
from pydantic import ValidationError

from app.core.config import JWT_TOKEN_PREFIX, JWT_SUBJECT, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.domain.users import User
from app.models.schemas.jwt import JWTMeta, JWTUser


def create_jwt_token(
    *, jwt_content: Dict[str, str], secret_key: str, expires_delta: timedelta
) -> str:
    to_encode = jwt_content.copy()
    logger.debug(to_encode)
    expire = datetime.utcnow() + expires_delta
    to_encode.update(JWTMeta(exp=expire, sub=JWT_SUBJECT).dict())
    return JWT_TOKEN_PREFIX + " " + jwt.encode(to_encode, secret_key, algorithm=JWT_ALGORITHM)


def create_access_token_for_user(user: User, secret_key: str) -> str:
    return create_jwt_token(
        jwt_content=JWTUser(username=user.username).dict(),
        secret_key=secret_key,
        expires_delta=timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
    )


def get_username_from_token(token: str, secret_key: str) -> str:
    try:
        # logger.debug("token", token)
        decode_str = jwt.decode(token, secret_key, algorithms=[JWT_ALGORITHM])
        logger.debug(decode_str)
        return JWTUser(**decode_str).username
    except jwt.PyJWTError as decode_error:
        raise ValueError("unable to decode JWT token") from decode_error
    except ValidationError as validation_error:
        raise ValueError("malformed payload in token") from validation_error
