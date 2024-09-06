from functools import wraps
import asyncio

from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse
from icmplib.exceptions import SocketPermissionError
from sqlalchemy.exc import NoResultFound

from errors.crud_errors import UserNotFoundInDb
from schemas.errors_schemas import ErrorMessage


def utils_errors_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except SocketPermissionError as ex:
            raise ex
        except OSError as ex:
            raise ex
        except Exception as ex:
            raise ex

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SocketPermissionError as ex:
            raise ex
        except OSError as ex:
            raise ex
        except Exception as ex:
            raise ex

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def crud_errors_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except NoResultFound as ex:
            raise UserNotFoundInDb from ex
        except Exception as ex:
            raise ex

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoResultFound as ex:
            raise UserNotFoundInDb from ex
        except Exception as ex:
            raise ex

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def dao_errors_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except UserNotFoundInDb as ex:
            raise ex
        except Exception as ex:
            raise ex

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UserNotFoundInDb as ex:
            raise ex
        except Exception as ex:
            raise ex

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def controller_errors_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except UserNotFoundInDb as ex:
            raise ex
        except Exception as ex:
            raise ex

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UserNotFoundInDb as ex:
            raise ex
        except Exception as ex:
            raise ex

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def router_error_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except UserNotFoundInDb:
            return JSONResponse(
                jsonable_encoder(ErrorMessage("User not found in database.")), 422
            )
        except Exception as ex:
            return JSONResponse(jsonable_encoder(ErrorMessage(str(ex))), 500)

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UserNotFoundInDb:
            return JSONResponse(
                jsonable_encoder(ErrorMessage("User not found in database.")), 422
            )
        except Exception as ex:
            return JSONResponse(jsonable_encoder(ErrorMessage(str(ex))), 500)

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def logging_dec(func):
    import time
    import logging

    logger = logging.getLogger("uvicorn")

    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        start_time: float = time.perf_counter()
        result = await func(*args, **kwargs)
        all_time: float = time.perf_counter() - start_time

        logger.info(f"{func.__name__} --- time {all_time} sec - ASYNC")
        return result

    @wraps(func)
    def inner_func(*args, **kwargs):
        start_time: float = time.perf_counter()
        result = func(*args, **kwargs)
        all_time: float = time.perf_counter() - start_time

        logger.info(f"{func.__name__} --- time {all_time} sec - SYNC")
        return result

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func
