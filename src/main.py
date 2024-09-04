from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from db.database import async_engine
from models.base_model import BaseModel

from api.routers.ping_router import router


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield


app = FastAPI(lifespan=app_lifespan)
app.include_router(router, prefix="/test")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
