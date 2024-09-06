from abc import ABC, abstractmethod
from uuid import UUID

from pydantic import BaseModel


class BaseDAO(ABC):
    @abstractmethod
    async def get_item(self, id: UUID) -> BaseModel:
        pass

    @abstractmethod
    async def get_all_items(self) -> list[BaseModel]:
        pass

    @abstractmethod
    async def add_item(self, data: BaseModel) -> bool:
        pass

    @abstractmethod
    async def add_many_items(self, data: list[BaseModel]) -> bool:
        pass

    @abstractmethod
    async def update_item(self, data: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    async def delete_item(self, id: UUID) -> BaseModel:
        pass
