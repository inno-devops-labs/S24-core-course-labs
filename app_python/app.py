from datetime import datetime
import pytz

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.head("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def display_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time_moscow = datetime.now(moscow_tz)
    formatted_time = current_time_moscow.strftime('%Y-%m-%d %H:%M:%S %Z')
    return f"Current time in Moscow: {formatted_time}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
