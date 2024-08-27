from typing import Any

from db.models.model_base import ModelBase


class PingModel(ModelBase):
    id: int = 0
    url: str = ""
    is_available: bool = True
    ping: str = "NaN"
    time: str = ""

    def __init__(self):
        pass

    def get_fields(self) -> list[Any]:
        return super().get_fields()
    
    def get_values(self) -> list[Any]:
        return super().get_values()
