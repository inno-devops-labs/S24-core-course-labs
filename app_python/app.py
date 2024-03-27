import datetime
import fastapi
import fastapi.templating as templating
import prometheus_client
import pytz

templates = templating.Jinja2Templates(directory="templates")

app = fastapi.FastAPI()

metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/api/time")
def fetch_time():
    now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    return now.strftime("%d-%m-%Y %H:%M:%S")


@app.get("/")
def read_root(request: fastapi.Request):
    return templates.TemplateResponse(
            request=request, name="time.html", context={"time": fetch_time()}
    )
