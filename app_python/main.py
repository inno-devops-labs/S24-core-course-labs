from fastapi import FastAPI
import pytz
from fastapi import Request
from datetime import datetime
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

template = Jinja2Templates(directory="template")


@app.get("/")
def read_root(request: Request):
    current_time_moscow = datetime.now(pytz.timezone(
        'Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")
    with open("counter.txt", "a+") as f:
        f.write("x\n")
    return template.TemplateResponse(request, "index.html", {"current_time": current_time_moscow})

@app.get("/visits")
async def visits() -> int:
    """
    Count visits to the application.
    :return: The number of visits.
    :rtype: int
    """
    with open("counter.txt", "r") as f:
        visits = len(f.readlines())
    return visits