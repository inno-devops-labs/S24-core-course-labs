from fastapi import FastAPI

from app.controllers import time
from app.controllers import meta

tags_metadata = [
    {
        "name": "time",
        "description": "Operations with time",
    },
    {
        "name": "meta",
        "description": "Meta-operations with app"
    }
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(time.router)
app.include_router(meta.router)
