from typing import Any
from dao.dao_base import DaoBase
from dao.result_dao import ResultDAO
from db.models.alchemy_models import PingModel
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
        self.path_file: str = "src/files/urls.txt"
        self.result_dao: DaoBase = ResultDAO()

    @controllers_handler
    async def get_all_func(self, table) -> list[Any]:
        return []

    @controllers_handler
    async def get_by_id_func(self, table, id: int) -> Any:
        return await self.result_dao.get_data_by_id(table, id)

    @controllers_handler
    def delete_by_id_func(self, table, id: int) -> bool:
        return self.result_dao.delete_by_id(table, id)

    @controllers_handler
    def test_func(self, table=PingModel) -> list[PingModel]:
        urls_list: list[str] = read_file(self.path_file)
        result: list[PingModel] = check_pings(urls_list)

        for ping_model in result:
            self.result_dao.add_data_to_db(table, ping_model)

        return result

    @controllers_handler
    async def async_test_func(self, table=PingModel) -> list[PingModel]:
        urls_list: list[str] = await async_read_file(self.path_file)
        ping_models: list[PingModel] = await async_check_pings(urls_list)

        await self.result_dao.async_add_many_data_to_db(ping_models)

        return ping_models
