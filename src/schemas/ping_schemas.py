from dataclasses import dataclass
from typing import List
from uuid import uuid4
from pydantic import BaseModel, UUID4


@dataclass
class Ping(BaseModel):
    def __init__(self):
        return super().__init__()

    id: UUID4 = uuid4()
    url: str = "example.com"
    is_available: bool = True
    ping: str = "102"

    class Config:
        from_attributes = True


@dataclass
class Result(BaseModel):
    def __init__(self, pings, total_pings_time):
        return super().__init__(pings=pings, total_pings_time=total_pings_time)

    pings: List[Ping]
    total_pings_time: str = "102 sec"


@dataclass
class DeleteResult(BaseModel):
    def __init__(self, success_status):
        return super().__init__(success_status=success_status)

    success_status: bool = True
