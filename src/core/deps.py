from db.database import async_session_local, session_local


async def async_get_db():
    async with async_session_local() as session:
        yield session
        await session.commit()


def get_db():
    with session_local() as session:
        yield session
        session.commit()
