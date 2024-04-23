import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_client import Counter, generate_latest
from time_manager import get_current_time

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

if not os.path.exists("./data/visits"):
    os.mkdir("data")
    with open("./data/visits", "a+") as f:
        f.write("0")

index_requests_total = Counter(
    "index_requests_total",
    "The number of requests to index page.",
)


@app.get("/", response_class=HTMLResponse)
def time(request: Request):
    index_requests_total.inc()
    with open("./data/visits", "w") as f:
        f.write(str(index_requests_total._value.get()))
    return templates.TemplateResponse(
        request=request, name="index.html",
        context={"time": get_current_time()}
    )


@app.get("/metrics")
def metrics():
    return generate_latest()


@app.get("/visits")
def visits(request: Request):
    with open("./data/visits", "r") as f:
        total_visits = f.read()
    return templates.TemplateResponse(
        request=request, name="visits.html",
        context={"counter": total_visits}
    )
