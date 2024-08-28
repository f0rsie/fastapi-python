import os
import re
import aiofiles
import datetime
import aioping
import math

from db.models.ping_model import PingModel


def check_ping(url):
    result = PingModel()
    result.time = datetime.datetime.now().strftime("%m/%d/%Y-%H-%M-%S")
    result.url = url

    full_string: str = os.popen(f"ping -c 1 {url}").read()
    compact_string: re.Match[str] | None = re.search(r"(time=).*.ms", full_string)

    if compact_string is not None:
        unformatted_ping = re.search(r"\d+.\d+", compact_string.group())

        if unformatted_ping is not None:
            result.ping = unformatted_ping.group(0)
            result.is_available = True

        else:
            result.is_available = False
            result.ping = "NaN"
    else:
        result.is_available = False
        result.ping = "NaN"

    return result


async def async_check_ping(url) -> PingModel:
    result = PingModel()
    try:
        result.time = datetime.datetime.now().strftime("%d/%m/%Y-%H-%M-%S")
        result.url = url

        delay = await aioping.ping(url, timeout=1) * 1000

        result.ping = round(delay, 2)
        result.is_available = True

    except Exception as ex:
        print(ex)
        result.ping = "NaN"
        result.is_available = False

    finally:
        return result


def read_file(filename):
    lines_result: list[str] = []
    with open(filename, mode="r") as file:
        for line in file:
            lines_result.append(line.replace("\n", ""))

    return lines_result


async def async_read_file(filename):
    lines_result: list[str] = []
    async with aiofiles.open(filename, mode="r") as file:
        async for line in file:
            lines_result.append(line.replace("\n", ""))

    return lines_result
