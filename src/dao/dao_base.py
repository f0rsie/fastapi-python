from abc import ABC, abstractmethod
from typing import Any

from db.models.ping_model import PingModel
from db.models.model_base import ModelBase


class DaoBase(ABC):
    @abstractmethod
    def add_data_to_db(self, table: ModelBase) -> bool:
        pass

    @abstractmethod
    def get_all_data_from_db(self) -> list[ModelBase]:
        pass

    @abstractmethod
    def delete_by(self, params: tuple[Any]) -> bool:
        pass

    @abstractmethod
    def delete_by_id(self, parameter: Any) -> bool:
        pass

    @abstractmethod
    def get_data_by_id(self, parameter: Any) -> list[ModelBase]:
        pass

    @abstractmethod
    def check_pings(self) -> list[PingModel]:
        pass

    @abstractmethod
    def check_and_save(self) -> list[ModelBase]:
        pass

    @abstractmethod
    async def async_check_pings(self) -> list[PingModel]:
        pass

    @abstractmethod
    async def async_check_and_save(self) -> list[ModelBase]:
        pass
