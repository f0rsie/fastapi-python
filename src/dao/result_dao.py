from typing import Any
from dao.dao_base import DaoBase
from db.db_base import DbBase
from db.db_pg import DbPg
from db.models.model_base import ModelBase
from exceptions.handlers import dao_handler


class ResultDAO(DaoBase):

    @dao_handler
    def __init__(self, db: DbBase = DbPg()):
        self.db: DbBase = db

    @dao_handler
    def add_data_to_db(self, table_name: str, data: ModelBase) -> bool:
        result: bool = self.db.add_to(table_name, data)
        return result

    @dao_handler
    def get_all_data_from_db(self, table_name: str) -> list[Any]:
        result: list[Any] = self.db.get_all(table_name)
        return result

    @dao_handler
    def delete_by_id(self, table_name: str, id: int) -> bool:
        result: bool = self.db.delete_by_id(table_name, id)
        return result

    @dao_handler
    def delete_by_sql_params(self, table_name: str, sql_params: str) -> bool:
        result: bool = self.db.delete_by_sql_params(table_name, sql_params)
        return result

    @dao_handler
    def get_data_by_id(self, table_name: str, id: int) -> Any:
        result: Any = self.db.get_by_id(table_name, id)
        return result
