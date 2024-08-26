import os
import re
import aiofiles
import datetime

from ping_model import PingModel

def check_ping(url):
    result = PingModel()
    result.logtime = datetime.datetime.now().strftime("%m/%d/%Y-%H-%M-%S")
    result.url = url

    full_string = os.popen(f"ping -c 1 {url}").read()
    compact_string = re.search(r"(time=).*.ms", full_string)

    if compact_string is not None:
        unformatted_ping = re.search(r"\d+.\d+", compact_string.group())

        if unformatted_ping is not None:
            result.ping_value = unformatted_ping.group(0)
            result.is_available = True

        else:
            result.is_available = False
    else:
        result.is_available = False

    return result

def read_file(filename):
    lines_result = []
    with open(filename, mode="r") as file:
        for line in file:
            lines_result.append(line.replace("\n", ""))

    return lines_result

async def read_file_async(filename):
    lines_result = []
    async with aiofiles.open(filename, mode="r") as file:
        async for line in file:
            lines_result.append(line.replace("\n", ""))

    return lines_result
