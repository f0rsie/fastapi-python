from abc import ABC, abstractmethod
from typing import Any
from db.models.model_base import ModelBase


class DbBase(ABC):
    @abstractmethod
    def conenct(self):
        pass

    @abstractmethod
    def get_all(self, table_name: str) -> list[Any]:
        pass

    @abstractmethod
    def get_by_id(self, table_name: str, id: int) -> Any:
        pass

    @abstractmethod
    def add_to(self, table_name: str, table: ModelBase) -> bool:
        pass

    @abstractmethod
    def delete_by_id(self, table_name: str, id: int) -> bool:
        pass

    @abstractmethod
    def delete_by_sql_params(self, table_name: str, sql_params: str) -> bool:
        pass
