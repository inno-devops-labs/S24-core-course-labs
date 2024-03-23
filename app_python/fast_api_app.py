from fastapi import FastAPI

from api import router as api_router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
app.include_router(api_router, prefix="/api")

Instrumentator().instrument(app).expose(app)
