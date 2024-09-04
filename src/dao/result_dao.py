from typing import Any
from dao.dao_base import DaoBase
from db.db_base import DbBase
from db.db_pg import DbPg
from db.db_alchemy import DbAlchemy
from db.models.alchemy_models import ModelBase
from exceptions.handlers import dao_handler


class ResultDAO(DaoBase):

    @dao_handler
    def __init__(self, db: DbBase = DbAlchemy()):
        self.db: DbBase = db

    @dao_handler
    def add_data_to_db(self, table, data) -> bool:
        result: bool = self.db.add_to(table, data)
        return result
    
    @dao_handler
    async def async_add_many_data_to_db(self, data):
        await self.db.add_many_to(data)

    @dao_handler
    def get_all_data_from_db(self, table) -> list[Any]:
        result: list[Any] = self.db.get_all(table)
        return result

    @dao_handler
    def delete_by_id(self, table, id: int) -> bool:
        result: bool = self.db.delete_by_id(table, id)
        return result

    @dao_handler
    async def get_data_by_id(self, table, id: int) -> Any:
        result: Any = await self.db.get_by_id(table, id)
        return result
