from abc import ABC, abstractmethod
from typing import Any
from db.models.alchemy_models import ModelBase


class DbBase(ABC):
    @abstractmethod
    def get_all(self, table) -> list[Any]:
        pass

    @abstractmethod
    def get_by_id(self, table, id: int) -> Any:
        pass

    @abstractmethod
    def add_to(self, table, data) -> bool:
        pass

    @abstractmethod
    async def add_many_to(self, data):
        pass

    @abstractmethod
    def delete_by_id(self, table, id: int) -> bool:
        pass
