from fastapi import APIRouter

from .time import router as time_router

router = APIRouter()

router.include_router(router=time_router, prefix="/time")
