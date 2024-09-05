from fastapi import FastAPI
import uvicorn


from api.routers.ping_router import router

app = FastAPI()
app.include_router(router, prefix="/test")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, reload_delay=5.0)
