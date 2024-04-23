import os
from datetime import datetime
from pytz import timezone
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import asyncio

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/visits")
async def get_visits():
    visits_file_path = f"{os.path.dirname(os.path.realpath(__file__))}/../data/visits.txt"
    try:
        with open(visits_file_path, "r") as f:
            visits = f.readline().strip()
            if visits is None or visits == "":
                visits = 0
            else:
                visits = int(visits)
    except IOError:
        visits = 0

    return JSONResponse(content={"visits": visits}, status_code=200)


@app.get("/moscow-time")
async def read_moscow_time():
    await add_visit()
    tz = timezone('Europe/Moscow')
    now = datetime.now(tz)

    return now


counter_lock = asyncio.Lock()
visits_file_path = f"{os.path.dirname(os.path.realpath(__file__))}/../../data/visits.txt"

if not os.path.exists(visits_file_path):
    with open(visits_file_path, "w") as f:
        f.write("0")


async def add_visit():
    async with counter_lock:
        try:
            with open(visits_file_path, "r") as f:
                visits = f.readline().strip()
                if visits is None or visits == "":
                    visits = 1
                else:
                    visits = int(visits) + 1
        except IOError:
            visits = 1
        with open(visits_file_path, "w") as f:
            f.writelines(str(visits))
