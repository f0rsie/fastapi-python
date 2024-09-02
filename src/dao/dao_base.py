from abc import ABC, abstractmethod
from typing import Any


class DaoBase(ABC):
    @abstractmethod
    def add_data_to_db(self, table, data) -> bool:
        pass

    @abstractmethod
    async def async_add_many_data_to_db(self, data):
        pass

    @abstractmethod
    def get_all_data_from_db(self, table) -> list[Any]:
        pass

    @abstractmethod
    def delete_by_id(self, table, id: int) -> bool:
        pass

    @abstractmethod
    def get_data_by_id(self, table, id: int) -> Any:
        pass
