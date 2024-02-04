from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pytz

server = FastAPI() # Create server


@server.get('/') 
def root():
    """
        Returns index.html after requesting root path ( example.com/ ).
    """
    return HTMLResponse(open('index.html').read()) # Return index.html


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