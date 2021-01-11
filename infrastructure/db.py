from typing import Optional

from application.repository import IUserRepository
from domain.entity import User

memdb = {"foo": {"id": "foo", "name": "bar", "age": 10}}


class UserRepository(IUserRepository):
    def find_by_id(id: str) -> Optional[User]:
        data = memdb.get(id)
        if data:
            return User(**data)
        else:
            return None