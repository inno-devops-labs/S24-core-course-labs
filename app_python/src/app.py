from datetime import datetime

from fastapi import FastAPI
from prometheus_client import make_asgi_app

from src.business_logic import get_current_moscow_time, get_human_readable_time

app = FastAPI(title="Moscow Time")

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/")
def index() -> str:
    current_date: datetime = get_current_moscow_time()
    human_readable: str = get_human_readable_time(current_date)

    return human_readable


@app.get("/health")
def health() -> str:
    return "OK"
