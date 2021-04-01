#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Descripttion: https://github.com/sxhxliang
# version: 0.0.1
# Author: Shihua Liang (sxhx.liang@gmail.com)
# FilePath: /manage-fastapi/fastapi-realworld-example-app-mysql/app/db/database.py
# Create: 2021-03-31 20:37:23
# LastAuthor: Shihua Liang
# lastTime: 2021-04-01 10:14:21
# --------------------------------------------------------


import re
import peewee
from contextvars import ContextVar
from fastapi import Depends

from playhouse.db_url import connect
from playhouse.pool import PooledMySQLDatabase

from app.core.config import HOST, USERNAME, PASSWORD, DATABASE, DATABASE_PREFIX, MAX_CONNECTIONS_COUNT, STALE_TIMEOUT

# Connect to the database URL defined in the environment, falling
# back to a local Sqlite database if no database URL is specified.

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

db = PooledMySQLDatabase(
        DATABASE,
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        max_connections=MAX_CONNECTIONS_COUNT,
        stale_timeout=STALE_TIMEOUT
    )

# https://fastapi.tiangolo.com/advanced/sql-databases-peewee/?h=before
class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

db._state = PeeweeConnectionState()


async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()

# http://docs.peewee-orm.com/en/latest/peewee/api.html#fields

SNAKE_CASE_STEP1 = re.compile('(.)_*([A-Z][a-z]+)')
SNAKE_CASE_STEP2 = re.compile('([a-z0-9])_*([A-Z])')

def make_table_name(model_class):
    model_name = model_class.__name__
    first = SNAKE_CASE_STEP1.sub(r'\1_\2', model_name)
    model_name = DATABASE_PREFIX + SNAKE_CASE_STEP2.sub(r'\1_\2', first).lower()
    print("model_name:", model_name)
    return  model_name

class BaseModel(peewee.Model):
    class Meta:
        database = db
        table_function = make_table_name


def create_tables():
    from app.db import schemas
    db.create_tables([schemas.User])
