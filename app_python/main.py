import datetime
import os
import threading
import time
from contextlib import asynccontextmanager

import ntplib
import pytz
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import Field
from pydantic_settings import BaseSettings

mutex = threading.Lock()


class Settings(BaseSettings):
    startup_time: float = Field(default=time.time())
    global_startup_time: float = Field(default=time.time())
    tz: pytz.BaseTzInfo = pytz.timezone("Europe/Moscow")


@asynccontextmanager
async def lifespan(app: FastAPI):
    ntp_client = ntplib.NTPClient()
    settings.startup_time = time.time()
    response = ntp_client.request("pool.ntp.org")
    settings.global_startup_time = float(response.tx_time)
    if not os.path.exists("/code/vol/visits"):
        with open("/code/vol/visits", "w") as visits_file:
            visits_file.write("0")
    else:
        with open("/code/vol/visits", "r") as visits_file_read:
            if not visits_file_read.read():
                with open("/code/vol/visits", "w") as visits_file:
                    visits_file.write("0")
    yield


settings = Settings()
app = FastAPI(lifespan=lifespan)
Instrumentator().instrument(app).expose(app)


@app.get(
    "/visits",
    status_code=200,
    description="""
    The endpoint that returns number of recorded visits.
    """,
)
async def get_recorded_visits_number():
    with open("/code/vol/visits", "r") as visits_file:
        return int(visits_file.read())


@app.get(
    "/",
    status_code=200,
    description="""
    The endpoint that returns the exact global Moscow time.
    """,
)
async def global_moscow_time():
    mutex.acquire()
    with open("/code/vol/visits", "r") as visits_file:
        num = int(visits_file.read())
    num += 1
    with open("/code/vol/visits", "w") as visits_file:
        visits_file.write(str(num))
    mutex.release()
    time_from_startup = time.time() - settings.startup_time
    global_time_seconds = time_from_startup + settings.global_startup_time
    return {
        "moscow_time": datetime.datetime.fromtimestamp(
            global_time_seconds, tz=settings.tz
        )
    }
