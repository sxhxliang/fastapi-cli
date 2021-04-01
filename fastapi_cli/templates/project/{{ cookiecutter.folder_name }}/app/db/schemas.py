#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Descripttion: https://github.com/sxhxliang
# version: 0.0.1
# Author: Shihua Liang (sxhx.liang@gmail.com)
# FilePath: /manage-fastapi/fastapi-realworld-example-app-mysql/app/db/schemas.py
# Create: 2021-03-31 20:45:31
# LastAuthor: Shihua Liang
# lastTime: 2021-04-01 10:23:39
# --------------------------------------------------------
import datetime
from peewee import *
from app.db.database import BaseModel

# define all database tables
# 用户
class User(BaseModel):
    id = AutoField()
    user_id = CharField(unique=True)
    username = CharField()
    user_phone = CharField()
    email = CharField()
    salt = CharField()
    hashed_password = CharField()
    bio = CharField(default="你好")
    image = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)