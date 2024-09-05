from typing import Any, List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_db, async_get_db
from controllers.ping_controller import PingController

from errors.error_handlers import router_error_handler

from schemas.ping_schemas import Ping, Result, DeleteResult
from schemas.errors_schemas import ErrorMessage


router = APIRouter()


responses: dict[int | str, dict[str, Any]] = {
    422: {
        "model": ErrorMessage("User not found in db."),
        "description": "User not found in db.",
    },
    500: {
        "model": ErrorMessage("Unknown server error."),
        "description": "Unknown server error.",
    },
}


@router.get("/test", response_model=Result, responses=responses)
@router_error_handler
def test(session: Session = Depends(get_db)):
    ping_controller = PingController(session)

    result: Result = ping_controller.test_func()

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.get("/a-test", response_model=Result, responses=responses)
@router_error_handler
async def async_test(session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result: Result = await ping_controller.async_test_func()

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.get("/pings/get-all", response_model=List[Ping], responses=responses)
@router_error_handler
async def async_get_all(session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result: list[Ping] = await ping_controller.get_all_func()

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.get("/pings/by-id", response_model=Ping, responses=responses)
@router_error_handler
async def async_get_by_id(id: str, session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result: Ping = await ping_controller.get_by_id_func(id)

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)


@router.delete("/pings/delete", response_model=DeleteResult, responses=responses)
@router_error_handler
async def async_delete_by_id(id: str, session: AsyncSession = Depends(async_get_db)):
    ping_controller = PingController(session)

    result = await ping_controller.delete_by_id_func(id)

    json_result = jsonable_encoder(result)
    return JSONResponse(json_result)
