import logging
import sys
from typing import List

from databases import DatabaseURL
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from app.core.logging import InterceptHandler

API_PREFIX = "/api"
VERSION = "1.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_URL: DatabaseURL = config("DB_CONNECTION", cast=DatabaseURL)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=32)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
STALE_TIMEOUT:str = config("STALE_TIMEOUT",cast=int,default=300)

HOST:str = config("HOST",cast=str,default="127.0.0.1")
PORT:int = config("PORT",cast=int,default=3306)
USERNAME:str = config("USERNAME",cast=str,default="root")
PASSWORD:str = config("PASSWORD",cast=str,default="")
DATABASE:str = config("DATABASE",cast=str,default="")
DATABASE_PREFIX:str = config("DATABASE_PREFIX",cast=str,default="")


# jwt authentication
JWT_SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)
JWT_TOKEN_PREFIX = "Token"  # noqa: S105 在做用户校验时，需要把这个前缀加上，并加空格
JWT_SUBJECT = "access"
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week


PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
