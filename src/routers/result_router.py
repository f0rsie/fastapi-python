from typing import Any
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from controllers.result_controller import ResultController
from db.models.alchemy_models import PingModel
from exceptions.handlers import routers_handler, logging_dec


try:
    result_router = APIRouter()
    result_controller: ResultController = ResultController()
except BaseException as ex:
    raise ex


@result_router.get("/test")
@routers_handler
def test():
    result: list[PingModel] = result_controller.test_func()
    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@result_router.get("/a-test")
@routers_handler
async def async_test():
    result: list[Any] = await result_controller.async_test_func()
    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@result_router.get("/pings/get-all")
@routers_handler
async def async_get_all(table):
    result = await result_controller.get_all_func(table)
    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@result_router.get("/pings/by-id")
@routers_handler
async def get_by_id(table, id: int):
    result: Any = result_controller.get_by_id_func(table, id)
    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@result_router.delete("/pings/delete")
@routers_handler
async def delete_by_id(table, id: int):
    result: bool = result_controller.delete_by_id_func(table, id)
    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)
