from pydantic import BaseModel


class PingsBaseModel(BaseModel):
    id: int | None
    url: str | None
    is_available: bool | None
    ping: str | None
    time: str | None
