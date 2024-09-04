from functools import wraps
import asyncio
import time
from fastapi.responses import JSONResponse
from psycopg2 import OperationalError
from icmplib.exceptions import SocketPermissionError

import logging

logger = logging.getLogger("uvicorn")


def utils_handler(func):
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


def db_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except OperationalError as ex:
            raise ex
        except Exception as ex:
            raise ex

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError as ex:
            raise ex
        except Exception as ex:
            raise ex

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def dao_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as ex:
            raise ex

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            raise ex

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def controllers_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as ex:
            raise ex

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            raise ex

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def routers_handler(func):
    @wraps(func)
    async def async_inner_func(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as ex:
            return JSONResponse(str(ex), status_code=500)

    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return JSONResponse(str(ex), status_code=500)

    if asyncio.iscoroutinefunction(func):
        return async_inner_func
    else:
        return inner_func


def logging_dec(func):
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
