import datetime
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Instrument the FastAPI app
instrumentator = Instrumentator()
instrumentator.instrument(app)
instrumentator.expose(app)

# Helper function to get current UTC time
def get_utc_now():
    return datetime.datetime.utcnow()

@app.get('/', response_class=HTMLResponse)
async def display_time(request: Request):
    try:
        moscow_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
        logging.info("Displayed Moscow time: %s", formatted_time)
        logging.info("Custom log message")

        return templates.TemplateResponse("index.html", {"request": request, "time": formatted_time})
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get('/error', response_class=HTMLResponse)
async def handle_error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0')
