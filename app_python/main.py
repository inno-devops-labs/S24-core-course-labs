from datetime import datetime, timezone, timedelta

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return f"""
    <html>
        <head>
            <title>Moscow Time</title>
        </head>
        <body>
        <h1>Current Moscow Time</h1>
        <p>
        {datetime.now(timezone(timedelta(hours=3))).strftime("%H:%M:%S")}
        </p>
        </body>
    </html>
    """
