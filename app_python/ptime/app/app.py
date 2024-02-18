from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.utils import get_formatted_time

app = FastAPI()
templates = Jinja2Templates(directory="ptime/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"time": get_formatted_time()}
    )
