from sqlalchemy import MetaData, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from models.base_model import BaseModel

class PingModel(BaseModel):
    __tablename__ = "pings"
    __table_args__ = {"schema": "fastapi"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, name="id")
    url: Mapped[str] = mapped_column(String(50), name="url")
    is_available: Mapped[bool] = mapped_column(name="is_available")
    ping: Mapped[str] = mapped_column(String(50), name="ping")
