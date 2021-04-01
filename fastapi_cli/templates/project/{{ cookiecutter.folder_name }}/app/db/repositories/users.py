import datetime
from typing import Optional,Any

from peewee import *
from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, UserInDB



from app.db.schemas import User

class UsersRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    async def get_user_by_email(self, *, email: str) -> UserInDB:
        user_row = User.select().where(User.email == email).dicts().get()
        if user_row:
            return UserInDB(**user_row)
        
        raise EntityDoesNotExist("user with email {0} does not exist".format(email))

    async def get_user_by_username(self, *, username: str) -> UserInDB:
        user_row = User.select().where(User.username == username).dicts().get()

        if user_row:
            return UserInDB(**user_row)

        raise EntityDoesNotExist(
            "user with username {0} does not exist".format(username)
        )

    async def create_user(
        self, *, username: str, email: str, password: str
    ) -> UserInDB:
        user = UserInDB(username=username, email=email)
        user.change_password(password)

        db_user = User(
                    username = user.username,
                    email=user.email,
                    salt=user.salt,
                    hashed_password=user.hashed_password)

        db_user.save()
        user_row = User.select().where(User.username == username).dicts().get()
        return user_row

    async def update_user(  # noqa: WPS211
        self,
        *,
        user: User,
        username: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        bio: Optional[str] = None,
        image: Optional[str] = None,
    ) -> UserInDB:
        # user_in_db = User.filter(User.username == username).first()

        user_in_db = User.select().where(User.username == username).dicts().get()

        user_in_db.username = username or user_in_db.username
        user_in_db.email = email or user_in_db.email
        user_in_db.bio = bio or user_in_db.bio
        user_in_db.image = image or user_in_db.image
        if password:
            user_in_db.change_password(password)
        
        now = datetime.datetime.now()
        user_in_db.updated_at = now.strftime("%Y-%m-%d %H:%M:%S")  
    
        user_in_db.save()
        return user_in_db
