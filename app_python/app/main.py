import os

from datetime import datetime, timezone, timedelta

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
file_path = "./visits"

@app.get("/visits", response_class=HTMLResponse)
async def read_visits():
    visits = 0

    if not os.path.exists(file_path): 
        with open(file_path, 'w') as file: 
            file.write("0")
    else:
        print("file exists")

    with open(file_path, 'r') as f:
        visits = f.read()
    return f"{visits}"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    visits = 0

    if not os.path.exists(file_path): 
        with open(file_path, 'w') as file: 
            file.write("0")
    else:
        print("file exists")


    with open(file_path, 'r') as f:
        visits = int(f.read())
    with open(file_path, 'w') as f:
        f.write(str(visits + 1))
    return f"""
    <html>
        <head>
            <title>Moscow Time</title>
        </head>
        <body>
        <h1>Current Moscow Time</h1>
        <p id="time">
        {datetime.now(timezone(timedelta(hours=3))).strftime("%H:%M:%S")}
        </p>
        </body>
    </html>
    """
