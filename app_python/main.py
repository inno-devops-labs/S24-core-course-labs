from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

from datetime import datetime
import pytz

app = FastAPI()
Instrumentator().instrument(app).expose(app)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def get_moscow_time():
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S")
    moscow_date = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%d.%m.%Y")
    return moscow_time, moscow_date


@app.get("/healthcheck")
async def healthcheck():
    return JSONResponse(content={"message": "OK"}, status_code=200)


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    date = get_moscow_time()

    return templates.TemplateResponse(
        request=request, name="index.html", context={"time": date[0], "date": date[1]}
    )
