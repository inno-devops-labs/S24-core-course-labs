"""
API routers for time logic.
"""

from app.api import di
from fastapi import APIRouter, Depends, responses

router = APIRouter()


@router.get('/', tags=["time"], response_class=responses.HTMLResponse)
async def show_time(time_manager = Depends(di.time_manager)):  # noqa: E251
    """Returns time taken from TimeManager with str format."""
    return await time_manager.str_datetime()
