from typing import Any
from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response

from db.models.model_base import ModelBase
from controllers.result_controller import ResultController
from db.models.ping_model import PingModel
from exceptions.handlers import routers_handler

try:
    result_router = APIRouter()
    result_controller = ResultController()
except:
    pass


@routers_handler
@result_router.get("/test")
def test():
    result: list[PingModel] = result_controller.test_func()
    return result


@routers_handler
@result_router.get("/a-test")
async def async_test():
    result: list[PingModel] = await result_controller.async_test_func()
    return result


@routers_handler
@result_router.get("/by-id")
def get_by_id(table: str, id: int):
    result: Any = result_controller.get_by_id_func(table, id)
    return JSONResponse(result)


@routers_handler
@result_router.delete("/delete")
def delete_by_id(table: str, id: int):
    result: bool = result_controller.delete_by_id_func(table, id)
    return JSONResponse(result)


@routers_handler
@result_router.delete("/delete-by-sql-params")
def delete_by_sql_params(table: str, sql_params: str):
    result: bool = result_controller.delete_by_sql_params_func(table, sql_params)
    return JSONResponse(result)
