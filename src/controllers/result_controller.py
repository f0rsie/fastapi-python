from typing import Any
from dao.dao_base import DaoBase
from dao.result_dao import ResultDAO
from db.db_pg import DbPg
from db.models.model_base import ModelBase
from db.models.ping_model import PingModel
from exceptions.handlers import controllers_handler
from utils import async_check_ping, async_read_file, check_ping, read_file


class ResultController:

    @controllers_handler
    def __init__(self):
        self.path_file: str = "files/urls.txt"
        self.result_dao: DaoBase = ResultDAO(DbPg())

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
        result: list[PingModel] = []
        url_list: list[str] = read_file(self.path_file)

        for url in url_list:
            url_PingModel: PingModel = check_ping(url)
            self.result_dao.add_data_to_db(table_name, url_PingModel)
            result.append(url_PingModel)

        return result

    @controllers_handler
    async def async_test_func(self, table_name: str = "pings") -> list[PingModel]:
        result: list[PingModel] = []
        url_list: list[str] = await async_read_file(self.path_file)

        for url in url_list:
            url_PingModel: PingModel = await async_check_ping(url)
            self.result_dao.add_data_to_db(table_name, url_PingModel)
            result.append(url_PingModel)

        return result
