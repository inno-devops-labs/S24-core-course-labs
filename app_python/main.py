from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime
import pytz

app = FastAPI()

MOSCOW_TZ = 'Europe/Moscow'

html_template = \
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Time in Moscow</title>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .time {{
                font-size: 72px;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="time">{time}</div>
    </body>
    </html>
    """


@app.get('/', response_class=HTMLResponse)
async def get_time(request: Request):
    """
    Function that gets invoked on loading index page

    @arg request: input request from a client
    @returns: HTMLResponse
    """
    moscow_time = datetime.now(pytz.timezone(MOSCOW_TZ)).strftime('%Y-%m-%d %H:%M:%S')
    return HTMLResponse(content=html_template.format(time=moscow_time), status_code=200)
