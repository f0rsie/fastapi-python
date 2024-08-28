from abc import ABC, abstractmethod
from typing import Any
from db.models.model_base import ModelBase


class DbBase(ABC):
    @abstractmethod
    def conenct(self):
        pass

    @abstractmethod
    def get_all(self, table_name: str) -> list[ModelBase]:
        pass

    @abstractmethod
    def get_by(self, table_name: str, parameters: dict[str, Any]) -> list[Any]:
        pass

    @abstractmethod
    def add_to(self, table_name: str, table: ModelBase) -> bool:
        pass

    @abstractmethod
    def delete_by(self, table_name: str, parameters: dict[str, Any]) -> bool:
        pass
