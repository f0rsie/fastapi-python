
from crud.ping_crud import PingCrud
from dao.base_dao import BaseDAO
from models.ping_model import PingModel


class PingDAO(BaseDAO):
    def __init__(self, session):
        self.session = session
        self.ping_crud = PingCrud(session)

    async def get_item(self, id: int) -> PingModel:
        result: PingModel = await self.ping_crud.get_item_by_id(id)
        return result
    
    async def get_all_items(self) -> list[PingModel]:
        result: list[PingModel] = await self.ping_crud.get_all_items()
        return result
    
    async def add_item(self, data: PingModel):
        await self.ping_crud.add_item(data)
        return True
    
    async def add_many_items(self, data: list[PingModel]):
        await self.ping_crud.add_items(data)
        return True
    
    async def update_item(self, data: PingModel) -> PingModel:
        result: PingModel = await self.ping_crud.update_item(data)
        return result
    
    async def delete_item(self, id: int):
        await self.ping_crud.delete_item_by_id(id)
        return True
