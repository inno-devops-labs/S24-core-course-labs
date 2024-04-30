from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.utils import get_formatted_time

app = FastAPI()
templates = Jinja2Templates(directory="ptime/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    with open("visits.txt", encoding="utf-8", mode="r+") as f:
        visits = 0
        string = f.read()
        if string != "":
            visits = int(string)
        visits += 1
        f.seek(0)
        f.write(str(visits))

    return templates.TemplateResponse(
        request=request, name="index.html", context={"time": get_formatted_time()}
    )


@app.get("/visits")
def visits():
    with open("visits.txt", encoding="utf-8", mode="r") as f:
        return f.readline()
