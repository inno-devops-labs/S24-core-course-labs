from fastapi import FastAPI
from pytz import timezone
from datetime import datetime
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/current_time")
def read_root():
    moscow_tz = timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    return {"Current Moscow Time": moscow_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}


@app.get("/")
def f():
    return FileResponse("index.html")
