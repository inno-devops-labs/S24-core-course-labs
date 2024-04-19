"""
API routers for time logic.
"""

from fastapi import APIRouter, Depends, responses

from app.api import di
from app.domain import time, visits

router = APIRouter()


@router.get("/", tags=["time"], response_class=responses.HTMLResponse)
async def show_time(
    time_manager: time.TimeManager = Depends(di.time_manager),
    visits_storage: visits.VisitsStorage = Depends(di.visits_storage),
):
    """Returns time taken from TimeManager with str format."""
    await visits_storage.increment_data()
    return await time_manager.str_datetime()
