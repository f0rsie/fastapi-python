import os
import re
from typing import Any
import aiofiles
import datetime
import aioping

from db.models.ping_model import PingModel
from exceptions.handlers import utils_handler
from icmplib import ping
from icmplib.exceptions import DestinationUnreachable, NameLookupError


# TODO: Перенести result: PingModel в сигнатуру функции, чтобы в дальнейшем перенести все except в handlers (decorator)
@utils_handler
def check_ping(url):
    try:
        result = PingModel()
        result.time = datetime.datetime.now().strftime("%m/%d/%Y-%H-%M-%S")
        result.url = url

        host = ping(url, 2, 1)
        result.ping = str(round(host.avg_rtt, 2))
        result.is_available = True

        return result
    except DestinationUnreachable:
        result.ping = "NaN"
        result.is_available = False

        return result
    except NameLookupError:
        result.ping = "NaN"
        result.is_available = False

        return result


@utils_handler
async def async_check_ping(url) -> PingModel:
    try:
        result = PingModel()
        result.time = datetime.datetime.now().strftime("%m/%d/%Y-%H-%M-%S")
        result.url = url

        delay: Any = await aioping.ping(url, timeout=3) * 1000

        result.ping = round(delay, 2)
        result.is_available = True

        return result

    except Exception:
        result.ping = "NaN"
        result.is_available = False

        return result


@utils_handler
def read_file(filename):
    lines_result: list[str] = []
    with open(filename, mode="r") as file:
        for line in file:
            lines_result.append(line.replace("\n", ""))

    return lines_result


@utils_handler
async def async_read_file(filename):
    lines_result: list[str] = []
    async with aiofiles.open(filename, mode="r") as file:
        async for line in file:
            lines_result.append(line.replace("\n", ""))

    return lines_result
