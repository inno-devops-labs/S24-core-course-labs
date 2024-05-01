import datetime
import fastapi
import fastapi.templating as templating
import prometheus_client
import pytz
import os

VISITS_FILE = "/app_python/vol/visits"

templates = templating.Jinja2Templates(directory="templates")

app = fastapi.FastAPI()

metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/api/time")
def fetch_time():
    now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    return now.strftime("%d-%m-%Y %H:%M:%S")

@app.get('/visits')
def show_visits():
    return f"{get_visits()}"

def increment_visits():
    cnt = 0
    try:
        with open(VISITS_FILE, 'r') as file:
            content = file.read()
            if content != '':
                cnt = int(content)
    except FileNotFoundError:
        pass
    with open(VISITS_FILE, 'w') as file:
        file.write(str(cnt + 1))


def get_visits():
    with open(VISITS_FILE, 'r') as file:
        return int(file.read())

@app.get("/")
def read_root(request: fastapi.Request):
    increment_visits()
    return templates.TemplateResponse(
            request=request, name="time.html", context={"time": fetch_time()}
    )
