from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import timezone

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    print(request.headers)
    return templates.TemplateResponse(
        request=request, name="webprint.j2", context={"text": "hello there"}
    )


@app.get("/time")
def read_time(request: Request):
    time = timezone.getMskTime()
    print(request.headers)
    print(time)

    return templates.TemplateResponse(
        request=request,
        name="webprint.j2",
        context={
            "text": time,
            "title": "Time",
        },
    )
