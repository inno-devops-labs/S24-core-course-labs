from datetime import datetime
import os

import pytz
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_current_time():
    """
    Return current time in Moscow in format YYYY-MM-DD HH:MM:SS.
    """
    moscow_tz = pytz.timezone("Europe/Moscow")
    return {"time": datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", default=8080))
    host = os.getenv("HOST", default="0.0.0.0")

    uvicorn.run(app, port=port, host=host)
