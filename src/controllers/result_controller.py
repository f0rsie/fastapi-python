from typing import Any
from dao.dao_base import DaoBase
from dao.result_dao import ResultDAO
from db.models.ping_model import PingModel
from exceptions.handlers import controllers_handler
from utils import (
    async_read_file,
    check_pings,
    read_file,
    async_check_pings,
)


class ResultController:

    @controllers_handler
    def __init__(self):
        self.path_file: str = "files/urls.txt"
        self.result_dao: DaoBase = ResultDAO()

    @controllers_handler
    async def get_all_func(self, table: str) -> list[Any]:
        return []

    @controllers_handler
    def get_by_id_func(self, table: str, id: int) -> Any:
        return self.result_dao.get_data_by_id(table, id)

    @controllers_handler
    def delete_by_id_func(self, table: str, id: int) -> bool:
        return self.result_dao.delete_by_id(table, id)

    @controllers_handler
    def delete_by_sql_params_func(self, table: str, sql_params: str) -> bool:
        return self.result_dao.delete_by_sql_params(table, sql_params)

    @controllers_handler
    def test_func(self, table_name: str = "pings") -> list[PingModel]:
        urls_list: list[str] = read_file(self.path_file)
        result: list[PingModel] = check_pings(urls_list)

        for ping_model in result:
            self.result_dao.add_data_to_db(table_name, ping_model)

        return result

    @controllers_handler
    async def async_test_func(self, table_name: str = "pings") -> list[PingModel]:
        urls_list: list[str] = await async_read_file(self.path_file)
        result: list[PingModel] = await async_check_pings(urls_list)

        for ping_model in result:
            self.result_dao.add_data_to_db(table_name, ping_model)

        return result
