from dataclasses import dataclass
import datetime


@dataclass
class PingModel:
    url: str = ""
    ping_value: str = "NaN"
    logtime: str = ""
    is_available: bool = True

    def __init__(self):
        pass
