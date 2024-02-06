from datetime import datetime

from fastapi import FastAPI

from src.business_logic import get_current_moscow_time, get_human_readable_time

app = FastAPI(title="Moscow Time")


@app.get("/")
def index() -> str:
    current_date: datetime = get_current_moscow_time()
    human_readable: str = get_human_readable_time(current_date)

    return human_readable
