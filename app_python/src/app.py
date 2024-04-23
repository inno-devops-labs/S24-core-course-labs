from datetime import datetime

import os

import uvicorn
from fastapi import FastAPI
from prometheus_client import make_asgi_app

from src.business_logic import get_current_moscow_time, get_human_readable_time

app = FastAPI(title="Moscow Time")

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


def _increment_visits() -> None:
    with open("/code/visits_folder/visits", "r") as visits_file:
        visits = int(visits_file.readline())
    with open("/code/visits_folder/visits", "w") as visits_file:
        visits_file.write(str(visits + 1))


@app.get("/")
def index() -> str:
    _increment_visits()

    current_date: datetime = get_current_moscow_time()
    human_readable: str = get_human_readable_time(current_date)

    return human_readable


@app.get("/health")
def health() -> str:
    _increment_visits()

    return "OK"


@app.get("/visits")
def get_visits() -> int:
    _increment_visits()

    with open("/code/visits_folder/visits") as visits_file:
        visits = int(visits_file.readline())

    return visits


def _create_visit():
    init_value = 0
    if not os.path.isfile("/code/visits_folder/visits"):
        with open("/code/visits_folder/visits", "w+") as file:
            file.write(str(init_value))


if __name__ == "__main__":
    _create_visit()
    uvicorn.run("src.app:app", host="0.0.0.0")
