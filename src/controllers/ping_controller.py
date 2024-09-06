from time import perf_counter
from uuid import UUID
from schemas.ping_schemas import DeleteResult, Result, Ping

from dao.base_dao import BaseDAO
from dao.ping_dao import PingDAO

from utils.utils import read_file, async_read_file, check_pings, async_check_pings

import asyncio

from core.config import settings

from controllers.base_controller import BaseController


class PingController(BaseController):
    def __init__(self, session):
        self.ping_dao: BaseDAO = PingDAO(session)

    def test_func(self) -> Result:
        start_time: float = perf_counter().real

        urls_list: list[str] = read_file(settings.URLS_FILE_PATH)
        pings_list: list[Ping] = check_pings(urls_list)

        total_time: float = perf_counter().real - start_time

        asyncio.run(self.ping_dao.add_many_items(pings_list))

        result = Result(pings_list, f"{round(total_time, 2)} sec")

        return result

    async def async_test_func(self) -> Result:
        start_time: float = perf_counter().real

        urls_list: list[str] = await async_read_file(settings.URLS_FILE_PATH)
        pings_list: list[Ping] = await async_check_pings(urls_list)

        total_time: float = perf_counter().real - start_time

        await self.ping_dao.add_many_items(pings_list)

        result = Result(pings_list, f"{round(total_time, 2)} sec")

        return result

    async def get_all_func(self) -> list[Ping]:
        result_list: list[Ping] = await self.ping_dao.get_all_items()

        return result_list

    async def get_by_id_func(self, id: UUID) -> Ping:
        result: Ping = await self.ping_dao.get_item(id)

        return result

    async def delete_by_id_func(self, id: UUID):
        result: DeleteResult = await self.ping_dao.delete_item(id)

        return result
