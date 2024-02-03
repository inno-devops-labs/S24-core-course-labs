from fastapi import FastAPI
from datetime import datetime
from starlette.responses import FileResponse
import pytz

app = FastAPI()

moscow_time_zone = pytz.timezone("Europe/Moscow")


@app.get("/")
async def root() -> FileResponse:
    return FileResponse('view/index.html')


@app.get("/api/time")
async def get_time() -> dict:
    return {'time': datetime.now(tz=moscow_time_zone).strftime("%H:%M:%S")}
