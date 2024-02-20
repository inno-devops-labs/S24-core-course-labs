from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from time_manager import get_current_time

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def time(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html",
        context={"time": get_current_time()}
    )
