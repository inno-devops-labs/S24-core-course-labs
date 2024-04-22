"""
This is the main module where the web app's application lives, gets setup and listens.
"""

from datetime import datetime
import pytz
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from prometheus_client import generate_latest


app = FastAPI()


async def getVisitCount():
    try:
        with open("visits.txt", "r") as file:
            return int(file.read())
    except Exception as e:
        return -1
    
async def incrementVisitCount():
    try:
        with open("visits.txt", "r") as file:
            visits = int(file.read())
    except Exception as e:
        visits = 0
    visits += 1
    with open("visits.txt", "w") as file:
        file.write(str(visits))



@app.get("/visits")
async def visits():
    await incrementVisitCount()
    return {"visits": await getVisitCount()}

@app.get("/metrics")
async def metric():
    return Response(content = generate_latest())


@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Endpoint that returns the current time and date in Moscow in HTML format.

    Accessing this endpoint renders an HTML page with a heading indicating
    it displays the current time in Moscow, followed by a paragraph showing
    the actual time. The time is displayed in the format "YYYY-MM-DD HH:MM:SS".

    Returns:
        HTMLResponse: An HTML page detailing the current time and date in Moscow.
    """
    await incrementVisitCount()
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
    <html>
        <head>
            <title>Current Time and Date in Moscow</title>
        </head>
        <body>
            <h1>Current Time in Moscow</h1>
            <p>{moscow_time}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


