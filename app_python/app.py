from datetime import datetime, timezone, timedelta
import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import uvicorn

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VISITS_FILE = "visits.txt"

app = FastAPI()
templates = Jinja2Templates(directory="templates")


if not os.path.exists(VISITS_FILE):
    with open(VISITS_FILE, "w") as file:
        file.write("0")

def get_visits_count():
    with open(VISITS_FILE, "r") as file:
        visits = int(file.read())
    return visits

def increment_visits_count():
    with open(VISITS_FILE, "r") as file:
        visits = get_visits_count()
    with open(VISITS_FILE, "w") as file:
        visits += 1
        file.write(str(visits))

@app.get("/")
async def read_root():
    moscow_time = datetime.now(timezone.utc) + timedelta(hours=3) 
    increment_visits_count()
    return {"Moscow Time": moscow_time, "Visits": get_visits_count()}

@app.get("/visits")
async def read_visits():
    increment_visits_count()
    return {"Visits": get_visits_count()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)