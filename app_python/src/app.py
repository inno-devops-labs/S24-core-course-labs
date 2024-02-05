from datetime import datetime
from pytz import timezone
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/moscow-time")
def read_moscow_time():
    tz = timezone('Europe/Moscow')
    now = datetime.now(tz)

    return now
