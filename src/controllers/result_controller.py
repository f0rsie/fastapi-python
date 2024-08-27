from fastapi import APIRouter

from dao.result_dao import ResultDAO
from dao.dao_base import DaoBase
from db.db_pg import DbPg
from db.models.model_base import ModelBase

result_router = APIRouter()

dao_model: DaoBase = ResultDAO(DbPg(), "files/urls.txt")


@result_router.get("/test")
def test():
    try:
        result: list[ModelBase] = dao_model.check_and_save()

        return result

    except Exception as ex:
        return ex


@result_router.get("/a-test")
async def async_test():
    try:
        result: list[ModelBase] = dao_model.check_and_save()

        return result

    except Exception as ex:
        return ex


@result_router.get("/{id}")
async def get_by_id(id: int):
    try:
        result: list[ModelBase] = dao_model.get_data_by_id(id)

        return result

    except Exception as ex:
        return ex
