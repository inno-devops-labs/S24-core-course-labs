from datetime import datetime

import pytz
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def msc_time_root(request: Request):
    try:
        moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%H:%M:%S %Y-%m-%d ")
        return templates.TemplateResponse("index.html", {"request": request, "current_time": moscow_time})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
