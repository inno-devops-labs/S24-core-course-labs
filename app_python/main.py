from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator
import os

from datetime import datetime
import pytz

app = FastAPI()
Instrumentator().instrument(app).expose(app)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
visits_file_path = "./visits/visits.txt"


def get_moscow_time():
    increment_visits()
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")
    moscow_date = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%d.%m.%Y")
    return moscow_time, moscow_date


count = 0

def increment_visits():
    global count
    count += 1
    if not os.path.exists('visits'):
        os.makedirs('visits', mode=0o777)
    with open("visits/visits.txt", "w+") as f:
        f.write(str(count))

@app.get("/visits")
def visits():
    with open("visits/visits.txt", "r") as f:
        return {'visits': int(f.read())}


@app.get("/healthcheck")
async def healthcheck():
    return JSONResponse(content={"message": "OK"}, status_code=200)


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    date = get_moscow_time()

    return templates.TemplateResponse(
        request=request, name="index.html", context={"time": date[0], "date": date[1]}
    )
