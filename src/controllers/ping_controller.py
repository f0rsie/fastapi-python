import utils

import asyncio

from models.ping_model import PingModel

from core.config import settings

from controllers.base_controller import BaseController
from dao.ping_dao import PingDAO

class PingController(BaseController):
    def __init__(self, session):
        self.ping_dao = PingDAO(session)

    def test_func(self) -> list[PingModel]:
        urls_list: list[str] = utils.read_file(settings.URLS_FILE_PATH)
        result_list: list[PingModel] = utils.check_pings(urls_list)

        asyncio.run(self.ping_dao.add_many_items(result_list))

        return result_list 
    
    async def async_test_func(self) -> list[PingModel]:
        urls_list: list[str] = await utils.async_read_file(settings.URLS_FILE_PATH)
        result_list: list[PingModel] = await utils.async_check_pings(urls_list)

        await self.ping_dao.add_many_items(result_list)
        
        return result_list
    
    async def get_all_func(self) -> list[PingModel]:
        result_list: list[PingModel] = await self.ping_dao.get_all_items()

        return result_list
    
    async def get_by_id_func(self, id: int) -> PingModel:
        result: PingModel = await self.ping_dao.get_item(id)

        return result
    
    async def delete_by_id_func(self, id: int):
        result = await self.ping_dao.delete_item(id)
        
        return result
