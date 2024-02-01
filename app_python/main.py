from fastapi import FastAPI
import pytz
from fastapi import Request
from datetime import datetime
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="template")


@app.get("/")
def read_root(request: Request):
    current_time_moscow = datetime.now(pytz.timezone(
        'Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S")
    return template.TemplateResponse(request, "index.html", {"current_time": current_time_moscow})
