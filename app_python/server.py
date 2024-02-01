from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pytz

server = FastAPI()


@server.get('/')
def root():
    return HTMLResponse(open('index.html').read())


@server.get('/time')
def time():
    msk_tz = pytz.timezone('Europe/Moscow')
    time = datetime.now(msk_tz)
    return {
        'time': time.strftime("%H:%M:%S")
    }