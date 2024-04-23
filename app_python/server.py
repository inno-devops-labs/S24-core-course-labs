import os
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pytz

server = FastAPI() # Create server

templates = Jinja2Templates(directory='./')

@server.get('/') 
def root():
    """
        Returns index.html after requesting root path ( example.com/ ).
    """
    return HTMLResponse(open('index.html').read(), media_type="text/html") # Return index.html


@server.get('/time')
def time():
    """
        Returns current Moscow time in JSON format.
    """
    msk_tz = pytz.timezone('Europe/Moscow') # Get Moscow timezone
    time = datetime.now(msk_tz) # Get current time in Moscow
    return {
        'time': time.strftime("%H:%M:%S")  # Return current Moscow Time in format HH:MM:SS
    }

def add_visit():
    os.makedirs('data', exist_ok=True)
    if not os.path.exists('data/visits'):
        f = open('data/visits', 'w')
        f.write('0')
        f.flush()
        f.close()
    visits = int(open('data/visits').read())
    visits += 1
    with open('data/visits', 'w') as f:
        f.write(str(visits))
    return visits

@server.get('/visits')
def visits(request: Request):
    visits = add_visit()
    return templates.TemplateResponse(request=request, name='visit.html', context={'visits': visits})