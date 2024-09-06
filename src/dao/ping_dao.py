from uuid import uuid4
from crud.ping_crud import PingCrud
from dao.base_dao import BaseDAO
from schemas.ping_schemas import DeleteResult, Ping
from models.db.ping_orm_model import PingOrmModel


class PingDAO(BaseDAO):
    def __init__(self, session):
        self.session = session
        self.ping_crud = PingCrud(session)

    async def get_item(self, id: str) -> Ping:
        crud_result: PingOrmModel = await self.ping_crud.get_item_by_id(id)

        result: Ping = Ping.model_validate(crud_result)

        return result

    async def get_all_items(self) -> list[Ping]:
        crud_result: list[PingOrmModel] = await self.ping_crud.get_all_items()

        result: list[Ping] = [Ping.model_validate(x) for x in crud_result]

        return result

    async def add_item(self, data: Ping):
        data.id = uuid4()

        crud_input = PingOrmModel(data)

        await self.ping_crud.add_item(crud_input)
        return True

    async def add_many_items(self, data: list[Ping]):
        for item in data:
            item.id = uuid4()

        crud_input: list[PingOrmModel] = [PingOrmModel(x) for x in data]

        await self.ping_crud.add_items(crud_input)
        return True

    async def update_item(self, data: Ping) -> Ping:
        crud_result: PingOrmModel = await self.ping_crud.update_item(data)

        result: Ping = Ping.model_validate(crud_result)

        return result

    async def delete_item(self, id: str) -> DeleteResult:
        await self.ping_crud.delete_item_by_id(id)
        
        return DeleteResult(True)
