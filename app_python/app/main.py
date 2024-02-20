from fastapi import FastAPI

from app.controllers import time

tags_metadata = [
    {
        "name": "time",
        "description": "Operations with time",
    }
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(time.router)
