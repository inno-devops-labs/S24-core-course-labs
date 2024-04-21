"""Main file with / route."""

from datetime import datetime, timezone, timedelta
from prometheus_client import Counter, generate_latest

from fastapi import FastAPI

app = FastAPI()

request_counter = Counter(
    'request_counter',
    'The amount of times endpoint was called'
)


class VisitCounter:
    def __init__(self):
        f = open("visits.txt", "r")
        self.counter = int(f.readline())
        f.close()

    def inc(self):
        self.counter += 1
        f = open("visits.txt", "w")
        f.write(str(self.counter))
        f.close()

visit_counter = VisitCounter()

@app.get("/")
async def root():
    """Root endpoint."""
    request_counter.inc()
    visit_counter.inc()
    return {"current_time": datetime.now(timezone(timedelta(hours=3)))}


@app.get("/metrics")
def metrics():
    return generate_latest()
