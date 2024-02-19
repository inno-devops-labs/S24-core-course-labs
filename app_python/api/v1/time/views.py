from fastapi import APIRouter
from datetime import datetime, time
from zoneinfo import ZoneInfo

from api.v1.time.schemas import TimeResponse

router = APIRouter(tags=["Time"])


@router.get("/", response_model=TimeResponse)
async def get_time():
    return TimeResponse(time=datetime.now(tz=ZoneInfo("Europe/Moscow")).time())