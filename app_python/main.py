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
        mct = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

        client_host = request.client.host if request.client else "TestClient"
        logging.info(f"Request from {client_host}")
        logging.info(f"Returned time: {mct}")

        return templates.TemplateResponse(
            "time.html", {"request": request, "time": mct}
        )
    except Exception as e:
        print(e)
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
