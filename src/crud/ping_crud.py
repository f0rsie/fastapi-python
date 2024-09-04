from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query

from crud.base_crud import BaseCrud
from models.ping_model import PingModel


class PingCrud(BaseCrud):
    def __init__(self, session):
        self.session: AsyncSession = session

    async def get_item_by_id(self, id: int) -> PingModel:
        result: PingModel = await self.session.get_one(PingModel, id)
        return result
    
    async def get_all_items(self) -> list[PingModel]:
        result: list[PingModel] = list((await self.session.scalars(select(PingModel))).all())

        return result
    
    async def add_item(self, data: PingModel):
        self.session.add(data)
    
    async def add_items(self, data: list[PingModel]):
        self.session.add_all(data)
    
    async def delete_item_by_id(self, id: int):
        await self.session.delete(id) # сюда сущность передавать вместо id
    
    async def update_item(self, data: PingModel) -> PingModel:
        result: PingModel = await self.update_item(data)
        return result