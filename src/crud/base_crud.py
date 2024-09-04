from abc import ABC, abstractmethod

from models.base_model import BaseModel


class BaseCrud(ABC):
    @abstractmethod
    def get_item_by_id(self, id: int) -> BaseModel:
        pass

    @abstractmethod
    def get_all_items(self) -> list[BaseModel]:
        pass

    @abstractmethod
    def add_item(self, data: BaseModel):
        pass

    @abstractmethod
    def add_items(self, data: list[BaseModel]):
        pass

    @abstractmethod
    def delete_item_by_id(self, id: int):
        pass

    @abstractmethod
    def update_item(self, data: BaseModel) -> BaseModel:
        pass
