from abc import ABC, abstractmethod
from typing import Any

from db.models.ping_model import PingModel
from db.models.model_base import ModelBase


class DaoBase(ABC):
    @abstractmethod
    def add_data_to_db(self, table_name: str, data: ModelBase) -> bool:
        pass

    @abstractmethod
    def get_all_data_from_db(self, table_name: str) -> list[Any]:
        pass

    @abstractmethod
    def delete_by_sql_params(self, table_name: str, sql_params: str) -> bool:
        pass

    @abstractmethod
    def delete_by_id(self, table_name: str, id: int) -> bool:
        pass

    @abstractmethod
    def get_data_by_id(self, table_name: str, id: int) -> Any:
        pass
