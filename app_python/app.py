"""
Flask Application Module

This module contains the main Flask application for the project. It defines routes and handles
the application's behavior.

Author: Herman Dyudin
"""

from datetime import datetime, timezone, timedelta
import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

instrumentator = Instrumentator()
instrumentator.instrument(app)
instrumentator.expose(app)


@app.get('/', response_class=HTMLResponse)
async def display_time(request: Request):
    """
        Display Time Route
        This route displays the current time in Moscow. It calculates the current time in UTC,
        adjusts it to the Moscow timezone, and renders a template with the formatted time.

        Returns:
            str: Formatted string representing the current time.

        Author: Herman Dyudin
        """
    moscow_time = datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=3)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    logging.info("Displayed Moscow datetime: %s", formatted_time)
    logging.info("Custom log message")

    return templates.TemplateResponse("page.html", {"request": request, "time": formatted_time})


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=5000)
