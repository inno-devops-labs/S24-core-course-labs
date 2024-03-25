from datetime import datetime
from flask import Flask
import pytz
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
import uvicorn

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get("/msk_timezone")
def msk_timezone():
    time = datetime.now(pytz.timezone("Europe/Moscow"))
    return time.strftime("Current time (MSK timezone): %H:%M:%S")


@app.head("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
