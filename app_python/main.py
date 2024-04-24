import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone, timedelta
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

Instrumentator().instrument(app).expose(app)


# Setup Jinja2 templates location
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def show_time(request: Request):
    """
    Show the current time in Moscow timezone.
    """
    # Moscow timezone
    moscow_timezone = timezone(timedelta(hours=3))
    current_time = datetime.now(moscow_timezone).strftime("%H:%M:%S")

    with open('./volume/visits', 'r') as f:
        visits = int(f.read()) + 1
    with open('./volume/visits', 'w') as f:
        f.write(str(visits))

    # Pass the current time to the template
    return templates.TemplateResponse(
        "index.html", {"request": request, "current_time": current_time}
    )

@app.get("/visits")
async def show_visits():
    """
    Show the number of visits to the website.
    """
    with open('./volume/visits', 'r') as f:
        visits = int(f.read())

    # return as plain text without any templates
    return visits




if __name__ == "__main__":
    import uvicorn

    # Run the app with Uvicorn
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=int(os.environ.get("PORT", "5000")),
    )
