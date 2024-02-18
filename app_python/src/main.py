"""Main file with / route."""

from datetime import datetime, timezone, timedelta

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root endpoint."""
    return {"current_time": datetime.now(timezone(timedelta(hours=3)))}
