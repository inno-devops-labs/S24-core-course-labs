from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_client import Counter, Summary, generate_latest
from time_manager import get_current_time

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

index_requests_total = Counter(
    'index_requests_total',
    'The number of requests to index page.'
)

index_request_duration_seconds = Summary(
    'index_request_duration_seconds',
    'The duration of requests to index page.'
)


@app.get("/", response_class=HTMLResponse)
@index_request_duration_seconds.time()
def time(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html",
        context={"time": get_current_time()}
    )


@app.get("/metrics")
def metrics():
    return generate_latest()
