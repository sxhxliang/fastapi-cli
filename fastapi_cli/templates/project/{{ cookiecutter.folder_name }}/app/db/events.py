
import aiomysql
from fastapi import FastAPI
from loguru import logger

from app.core.config import DATABASE_URL
from app.db.database import (
    db, reset_db_state, get_db
)

from app.db import schemas


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to {0}", repr(DATABASE_URL))
    db.connect()
    # db.create_tables([schemas.User])

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")
    db.close()
    logger.info("Connection closed")
