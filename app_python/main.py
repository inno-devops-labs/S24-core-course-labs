from datetime import datetime
import os
import threading

import pytz
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator().instrument(app)
visits = 0
visits_mutex = threading.Lock()
visits_path = "data/visits"


def save_visits():
    try:
        os.mkdir("data")
    except Exception as err:
        print("err", err)
        pass

    with open(visits_path, "w") as visits_file:
        visits_file.write(str(visits))


def add_visits():
    global visits
    visits_mutex.acquire()
    visits += 1
    visits_mutex.release()
    save_visits()


@app.get("/")
def get_current_time():
    """
    Return current time in Moscow in format YYYY-MM-DD HH:MM:SS.
    """
    add_visits()

    moscow_tz = pytz.timezone("Europe/Moscow")
    return {"time": datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")}


@app.get("/visits")
def get_visits():
    add_visits()
    with open(visits_path, 'r') as f:
        total_visits = int(f.read())

    return {"visits": total_visits}


@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", default=8080))
    host = os.getenv("HOST", default="0.0.0.0")

    save_visits()
    uvicorn.run(app, port=port, host=host)
