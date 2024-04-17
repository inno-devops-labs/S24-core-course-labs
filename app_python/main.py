"""
The service that returns current time in Moscow in format YYYY-MM-DD HH:MM:SS.
"""

from datetime import datetime
import os

import pytz
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

VISITS_FILE_PATH = "data/visits.txt"

# Instrument the FastAPI app
Instrumentator().instrument(app).expose(app)


@app.get("/")
def get_current_time():
    """
    Return current time in Moscow in format YYYY-MM-DD HH:MM:SS.
    """
    increment_visits()
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}


@app.head("/health")
def health():
    """
    Return health status.
    """
    return {"status": "ok"}


@app.get("/visits")
def get_visits():
    """
    Return the number of visits.
    """
    with open(VISITS_FILE_PATH, "r") as file:
        visits = int(file.read())
    return {"visits": visits}


def increment_visits():
    with open(VISITS_FILE_PATH, "r+") as file:
        visits = int(file.read())
        visits += 1
        file.seek(0)
        file.write(str(visits))


def create_visits_file_if_not_exists():
    if os.path.isfile(VISITS_FILE_PATH):
        print("Visits file already exists")
        return

    init_value = 0
    with open(VISITS_FILE_PATH, "w+") as file:
        file.write(str(init_value))

    print(f"Visits file created with initial value {init_value}")


if __name__ == "__main__":
    import uvicorn

    create_visits_file_if_not_exists()
    uvicorn.run(app, port=80, host="0.0.0.0")
