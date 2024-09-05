from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from uuid import UUID

from models.db.base_orm_model import BaseOrmModel
from schemas.ping_schemas import Ping


class PingOrmModel(BaseOrmModel):
    __tablename__ = "pings"
    __table_args__ = {"schema": "fastapi"}

    id: Mapped[UUID] = mapped_column(name="id", primary_key=True)
    url: Mapped[str] = mapped_column(String(50), name="url")
    is_available: Mapped[bool] = mapped_column(name="is_available")
    ping: Mapped[str] = mapped_column(String(50), name="ping")

    def __init__(self, ping_model: Ping | None = None, **kw):
        if ping_model is not None:
            self.id = ping_model.id
            self.url = ping_model.url
            self.is_available = ping_model.is_available
            self.ping = ping_model.ping

        super().__init__(**kw)
