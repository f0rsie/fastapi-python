from abc import ABC, abstractmethod
from uuid import UUID

from models.db.base_orm_model import BaseOrmModel


class BaseCrud(ABC):
    @abstractmethod
    async def get_item_by_id(self, id: UUID) -> BaseOrmModel:
        pass

    @abstractmethod
    async def get_all_items(self) -> list[BaseOrmModel]:
        pass

    @abstractmethod
    async def add_item(self, data: BaseOrmModel):
        pass

    @abstractmethod
    async def add_items(self, data: list[BaseOrmModel]):
        pass

    @abstractmethod
    async def delete_item_by_id(self, id: UUID):
        pass

    @abstractmethod
    async def update_item(self, data) -> BaseOrmModel:
        pass
