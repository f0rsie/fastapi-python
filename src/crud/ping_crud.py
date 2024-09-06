from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from errors.error_handlers import crud_errors_handler

from crud.base_crud import BaseCrud
from models.db.ping_orm_model import PingOrmModel


class PingCrud(BaseCrud):
    def __init__(self, session):
        self.session: AsyncSession = session

    @crud_errors_handler
    async def get_item_by_id(self, id: UUID) -> PingOrmModel:
        result: PingOrmModel = await self.session.get_one(PingOrmModel, id)
        return result

    @crud_errors_handler
    async def get_all_items(self) -> list[PingOrmModel]:
        result: list[PingOrmModel] = list(
            (await self.session.scalars(select(PingOrmModel))).all()
        )
        return result

    @crud_errors_handler
    async def add_item(self, data: PingOrmModel):
        self.session.add(data)

    @crud_errors_handler
    async def add_items(self, data: list[PingOrmModel]):
        self.session.add_all(data)

    @crud_errors_handler
    async def delete_item_by_id(self, id: UUID):
        item: PingOrmModel = await self.session.get_one(PingOrmModel, id)
        await self.session.delete(item)

    @crud_errors_handler
    async def update_item(self, data) -> PingOrmModel:
        result: PingOrmModel = await self.update_item(data)
        return result
