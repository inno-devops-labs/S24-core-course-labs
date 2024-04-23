from datetime import datetime

import pytz
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./templates")
visits_file_path = "visits.txt"


@app.get("/")
async def msc_time_root(request: Request):
    try:
        moscow_time = (datetime.now(pytz.timezone("Europe/Moscow")).
                       strftime("%H:%M:%S %Y-%m-%d "))
        return templates.TemplateResponse(
            "index.html", {"request": request, "current_time": moscow_time}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/visits")
async def get_visits():
    try:
        with open(visits_file_path, "r") as file:
            visits = int(file.read())
        return {"visits": visits}
    except FileNotFoundError:
        return {"visits": 0}


@app.middleware("http")
async def add_visit_counter(request: Request, call_next):
    try:
        with open(visits_file_path, "r+") as file:
            visits = int(file.read())
            visits += 1
            file.seek(0)
            file.write(str(visits))
            file.truncate()
    except FileNotFoundError:
        with open(visits_file_path, "w") as file:
            file.write("1")
    response = await call_next(request)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
