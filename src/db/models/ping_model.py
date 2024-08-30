from db.models.model_base import ModelBase


class PingModel(ModelBase):
    id: int = 0
    url: str = ""
    is_available: bool
    ping: str
    time: str = ""

    def __init__(self):
        self.is_available = False
        self.ping = "0.0"
