from datetime import datetime

import pytz
from fastapi import FastAPI, HTTPException
from starlette.staticfiles import StaticFiles

app = FastAPI(title="Main app")
api = FastAPI(title="Api app")


@api.get("/time")
def get_time(tz: str):
    if tz not in pytz.all_timezones:
        raise HTTPException(status_code=400, detail=f"Unknown timezone {tz}")
    
    return {"time": datetime.now(pytz.timezone(tz)).strftime("%Y-%m-%d %H:%M:%S")}


app.mount("/api", api)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
