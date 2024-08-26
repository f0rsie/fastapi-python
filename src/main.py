from typing import Union
from fastapi import FastAPI
import uvicorn
from utils import read_file, check_ping, read_file_async
from db_work import DbWork

app = FastAPI()
db_work = DbWork()

url_file = "files/urls.txt"


@app.get("/test")
def test():
    urls = read_file(url_file)
    urls_pings = []

    for url in urls:
        url_ping_model = check_ping(url)
        urls_pings.append({f"{url_ping_model}"})
        db_work.add(url_ping_model)

    return {f"{urls_pings}"}


@app.get("/a-test")
async def a_test():
    urls = await read_file_async(url_file)
    urls_pings = []

    for url in urls:
        url_ping = check_ping(url)
        urls_pings.append({f"{url_ping}"})

    return {f"{urls_pings}"}

 #get /id

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
