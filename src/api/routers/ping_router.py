from typing import Any
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm.session import Session
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_db, async_get_db
from controllers.ping_controller import PingController
from models.ping_model import PingModel
from errors.error_handlers import routers_handler


router = APIRouter()


@router.get("/test")
@routers_handler
def test(session: Session = Depends(get_db)):
    ping_controller = PingController(session)

    result: list[PingModel] = ping_controller.test_func()

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.get("/a-test")
@routers_handler
async def async_test(session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result: list[Any] = await ping_controller.async_test_func()

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.get("/pings/get-all")
@routers_handler
async def async_get_all(session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result: list[PingModel] = await ping_controller.get_all_func()

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.get("/pings/by-id")
@routers_handler
async def get_by_id(id: int, session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result: PingModel = await ping_controller.get_by_id_func(id)

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.delete("/pings/delete")
@routers_handler
async def delete_by_id(id: int, session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result = await ping_controller.delete_by_id_func(id)

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)
