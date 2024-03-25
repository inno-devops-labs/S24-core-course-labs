from datetime import datetime
from fastapi import FastAPI
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get("/")
# Function which take MSK timezone
def msk_time():
    time = datetime.now(pytz.timezone('Europe/Moscow'))
    return time.strftime("Current time (MSK timezone): %H:%M:%S")


@app.head("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0')
