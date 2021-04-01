from typing import AsyncGenerator, Callable, Type

#from asyncpg.pool import Pool
# import aiomysql
# from aiomysql.pool import Pool
from fastapi import Depends
from starlette.requests import Request

from app.db.repositories.base import BaseRepository
from app.db.database import db, db_state_default


async def _reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def _get_db_pool(db_state=Depends(_reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()

def get_repository(repo_type: Type[BaseRepository]) -> Callable:  # type: ignore
    async def _get_repo() -> AsyncGenerator[BaseRepository, None]:
        with db.connection_context():
            yield repo_type()
    return _get_repo


