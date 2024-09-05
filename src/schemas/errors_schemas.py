from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class ErrorMessage(BaseModel):
    def __init__(self, message):
        return super().__init__(message=message)

    message: str = "Error"
