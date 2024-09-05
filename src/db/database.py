from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
)

from core.config import settings

engine: Engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
async_engine: AsyncEngine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_ASYNC_URI)
)

async_session_local = async_sessionmaker(
    bind=async_engine, autoflush=False, class_=AsyncSession, expire_on_commit=False
)

session_local = sessionmaker(
    bind=engine, autoflush=False, class_=Session, expire_on_commit=False
)
