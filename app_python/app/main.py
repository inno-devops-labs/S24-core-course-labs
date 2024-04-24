from fastapi import FastAPI
from datetime import datetime
from starlette.responses import FileResponse
from prometheus_fastapi_instrumentator import Instrumentator
import pytz

app = FastAPI()

moscow_time_zone = pytz.timezone("Europe/Moscow")
visits_file = "visits.txt"

instrumentator = Instrumentator().instrument(app)

try:
    with open(visits_file, "r") as f:
        visits_count = int(f.read())
except FileNotFoundError:
    visits_count = 0


@app.get("/")
async def root() -> FileResponse:
    global visits_count
    visits_count += 1
    with open(visits_file, "w") as f:
        f.write(str(visits_count))
    return FileResponse('view/index.html')


@app.on_event("startup")
async def on_startup():
    instrumentator.expose(app)


@app.get("/api/time")
async def get_time() -> dict:
    return {'time': datetime.now(tz=moscow_time_zone).strftime("%H:%M:%S")}

@app.get("/visits")
async def get_visits() -> dict:
    return {'visits': visits_count}
