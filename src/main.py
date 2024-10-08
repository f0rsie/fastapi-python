from fastapi import FastAPI
import uvicorn
from routers.result_router import result_router

app = FastAPI()
app.include_router(result_router, prefix="/test")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
