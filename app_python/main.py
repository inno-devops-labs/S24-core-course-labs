from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import pytz
import uvicorn
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get(
    "/",
    response_class=HTMLResponse,
)
def moscow_time(request: Request):
    try:
        moscow_tz = pytz.timezone("Europe/Moscow")
        moscow_current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

        logging.info(f"Request from {request.client.host}")
        logging.info(f"Returned time: {moscow_current_time}")

        return templates.TemplateResponse(
            "time.html", {"request": request, "time": moscow_current_time}
        )
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
