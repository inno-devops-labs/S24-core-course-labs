import os
import os.path
import pathlib
import threading
from datetime import datetime

import pytz
from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
from starlette.staticfiles import StaticFiles


class Visits:
    def __init__(self):
        self.mutex = threading.Lock()
        self.path = "data/visits"
        self.visits = 0

    def add(self):
        self.mutex.acquire()

        self.visits += 1
        self.save()

        self.mutex.release()

    def load(self):
        if not os.path.exists(self.path):
            return

        with open(self.path, "r") as f:
            self.visits = int(f.read())

    def save(self):
        try:
            os.mkdir("data")
        except:
            pass

        with open(self.path, "w") as visits_file:
            visits_file.write(str(self.visits))


dir_path = pathlib.Path(__file__).parent.resolve()

app = FastAPI(title="Main app")

instrumentator = Instrumentator().instrument(app)

api = FastAPI(title="Api app")


def get_time_with_tz(tz: str):
    return datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %H:%M:%S")


@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)


visits = Visits()
visits.load()


@api.get("/time")
def get_time(tz: str):
    visits.add()

    if tz not in pytz.all_timezones:
        raise HTTPException(status_code=400, detail=f"Unknown timezone {tz}")

    return {"time": get_time_with_tz(tz)}


@api.get("/visits")
def get_visits():
    visits.add()

    return {"visits": visits.visits}


app.mount("/api", api)
app.mount(
    "/",
    StaticFiles(directory=f"{dir_path}/static", html=True),
    name="static",
)
