"""Main file with / route."""

from datetime import datetime, timezone, timedelta
from prometheus_client import Counter, generate_latest

from fastapi import FastAPI

app = FastAPI()

request_counter = Counter(
        'request_counter',
        'The amount of times endpoint was called'
)

@app.get("/")
async def root():
    """Root endpoint."""
    request_counter.inc()
    return {"current_time": datetime.now(timezone(timedelta(hours=3)))}


@app.get("/metrics")
def metrics():
    return generate_latest()
