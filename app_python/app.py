from fastapi import FastAPI, HTTPException
from pytz import timezone
from datetime import datetime
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import prometheus_client

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

metrics_app = prometheus_client.make_asgi_app()
app.mount("/metrics", metrics_app)

VISITS_FILE_PATH = "/app/data/visits.txt"


def read_and_increment_visits():
    try:
        with open(VISITS_FILE_PATH, "r+") as file:
            visits = int(file.read().strip())
            visits += 1
            file.seek(0)
            file.write(str(visits))
            file.truncate()
            return visits
    except FileNotFoundError:
        with open(VISITS_FILE_PATH, "w") as file:
            file.write("1")
        return 1
    except ValueError:
        with open(VISITS_FILE_PATH, "w") as file:
            file.write("1")
        return 1


@app.middleware("http")
async def count_visits(request, call_next):
    read_and_increment_visits()
    response = await call_next(request)
    return response


@app.get("/current_time")
def read_root():
    moscow_tz = timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    return {"Current Moscow Time": moscow_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}


@app.get("/")
def f():
    return FileResponse("index.html")


@app.get("/visits")
def get_visits():
    try:
        with open(VISITS_FILE_PATH, "r") as file:
            visits = file.read().strip()
        return {"visits": visits}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Visits file not found")
