import abc
from typing import Optional

from domain.entity import User


class IUserRepository(abc.ABC):
    def find_by_id() -> Optional[User]:
        ...
