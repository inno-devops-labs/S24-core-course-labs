from datetime import datetime
import pathlib

import pytz
from fastapi import FastAPI, HTTPException
from starlette.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

dir_path = pathlib.Path(__file__).parent.resolve()

app = FastAPI(title="Main app")

instrumentator = Instrumentator().instrument(app)

api = FastAPI(title="Api app")


def get_time_with_tz(tz: str):
    return datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %H:%M:%S")


@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)


@api.get("/time")
def get_time(tz: str):
    if tz not in pytz.all_timezones:
        raise HTTPException(status_code=400, detail=f"Unknown timezone {tz}")

    return {"time": get_time_with_tz(tz)}


app.mount("/api", api)
app.mount(
    "/",
    StaticFiles(directory=f"{dir_path}/static", html=True),
    name="static",
)
