"""
The service that returns current time in Moscow in format YYYY-MM-DD HH:MM:SS.
"""

from datetime import datetime

import pytz
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_current_time():
    """
    Return current time in Moscow in format YYYY-MM-DD HH:MM:SS.
    """
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
