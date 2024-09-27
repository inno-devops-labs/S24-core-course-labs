import datetime
import fastapi
import fastapi.templating as templating
import pytz

templates = templating.Jinja2Templates(directory="templates")

app = fastapi.FastAPI()


@app.get("/api/time")
def fetch_time():
    now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    return now.strftime("%d-%m-%Y %H:%M:%S")


@app.get("/")
def read_root(request: fastapi.Request):
    return templates.TemplateResponse(
            request=request, name="time.html", context={"time": fetch_time()}
    )
