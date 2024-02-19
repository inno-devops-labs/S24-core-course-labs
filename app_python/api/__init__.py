from fastapi import APIRouter

from .v1 import router as api_v1_router

router = APIRouter()
router.include_router(router=api_v1_router, prefix="/v1")
