import os
from typing import Any

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from db.db_base import DbBase
from db.models.alchemy_models import PingModel
from db.models.alchemy_models import ModelBase
from exceptions.handlers import db_handler


class DbAlchemy(DbBase):

    @db_handler
    def __init__(self):
        self._async_config: URL = URL.create(
            drivername="postgresql+asyncpg",
            username=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=int(str(os.getenv("DB_PORT"))),
            database=os.getenv("POSTGRES_DB"),
        )
        self._config: URL = URL.create(
            drivername="postgresql",
            username=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=int(str(os.getenv("DB_PORT"))),
            database=os.getenv("POSTGRES_DB"),
        )

        self.async_engine: AsyncEngine = create_async_engine(self._async_config)
        self.engine: Engine = create_engine(self._config)

    @db_handler
    def get_all(self, table) -> list[Any]:
        return []

    @db_handler
    def get_by_id(self, table, id: int) -> Any:
        session = sessionmaker(autoflush=False, bind=self.engine)
        with self.engine.connect():
            with session() as db:
                result: Any = db.query(table).where(table.id == id).first()

                if result is None:
                    raise Exception("User not found")

                return result

    @db_handler
    def add_to(self, table, data):
        session = sessionmaker(autoflush=False, bind=self.engine)
        with session() as db:
            db.add(data)
            db.commit()

    @db_handler
    async def add_many_to(self, data):
        async_session = async_sessionmaker(autoflush=False, bind=self.async_engine)
        async with self.async_engine.connect():
            async with async_session() as session:
                session.add_all(data)
                await session.commit()

    @db_handler
    def delete_by_id(self, table, id: int) -> bool:
        return True
