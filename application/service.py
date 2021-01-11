from typing import Optional

import inject

from application.repository import IUserRepository
from domain.entity import User


class UserService:
    repo: IUserRepository = inject.attr(IUserRepository)

    def __init__(self, id: str):
        self._id = id

    def get_user(self) -> Optional[User]:
        return self.repo.find_by_id(self._id)