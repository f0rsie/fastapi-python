import aiofiles
from icmplib.models import Host

from icmplib import async_resolve, resolve, async_multiping, multiping
from icmplib.exceptions import NameLookupError

from core.config import settings

from models.ping_model import PingModel


def check_pings(urls: list[str]) -> list[PingModel]:
    results: list[PingModel] = []

    valid_urls: list[str] = url_validation(urls)

    host_list: list[Host] = multiping(valid_urls, 2, 1, privileged=settings.ROOT_PRIVILEGED)

    dictionary = dict(zip(valid_urls, host_list))

    for elem in dictionary:
        ping_model = PingModel()
        ping_model.url = elem
        ping_model.ping = str(round(dictionary[elem].avg_rtt, 2))
        ping_model.is_available = dictionary[elem].is_alive

        results.append(ping_model)

    unvalid_urls: list[str] = list(set(urls) - set(valid_urls))

    for url in unvalid_urls:
        ping_model = PingModel()
        ping_model.url = url
        ping_model.ping = "NaN"
        ping_model.is_available = False

        results.append(ping_model)

    return results


async def async_check_pings(urls: list[str]) -> list[PingModel]:
    results: list[PingModel] = []

    valid_urls: list[str] = await async_url_validation(urls)

    host_list: list[Host] = await async_multiping(
        valid_urls, 2, 1, privileged=settings.ROOT_PRIVILEGED
    )

    dictionary = dict(zip(valid_urls, host_list))

    for elem in dictionary:
        ping_model = PingModel()
        ping_model.url = elem
        ping_model.ping = str(round(dictionary[elem].avg_rtt, 2))
        ping_model.is_available = dictionary[elem].is_alive

        results.append(ping_model)

    unvalid_urls: list[str] = list(set(urls) - set(valid_urls))

    for url in unvalid_urls:
        ping_model = PingModel()
        ping_model.url = url
        ping_model.ping = "0.0"
        ping_model.is_available = False

        results.append(ping_model)

    return results


def url_validation(urls: list[str]) -> list[str]:
    results: list[str] = []

    for url in urls:
        try:
            resolve(url)
            results.append(url)
        except NameLookupError:
            continue

    return results


async def async_url_validation(urls: list[str]) -> list[str]:
    results: list[str] = []

    for url in urls:
        try:
            await async_resolve(url)
            results.append(url)
        except NameLookupError:
            continue

    return results


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
