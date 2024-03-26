from fastapi import FastAPI
from datetime import datetime
from starlette.responses import FileResponse
from prometheus_fastapi_instrumentator import Instrumentator
import pytz

app = FastAPI()

moscow_time_zone = pytz.timezone("Europe/Moscow")

instrumentator = Instrumentator().instrument(app)

@app.get("/")
async def root() -> FileResponse:
    return FileResponse('view/index.html')


@app.on_event("startup")
async def on_startup():
    instrumentator.expose(app)


@app.get("/api/time")
async def get_time() -> dict:
    return {'time': datetime.now(tz=moscow_time_zone).strftime("%H:%M:%S")}
