from pydantic import BaseModel, Field
from datetime import time, timezone, datetime
from zoneinfo import ZoneInfo


class TimeResponse(BaseModel):
    time_field: time = Field(datetime.now(tz=ZoneInfo(key="Europe/Moscow")).time(), alias="time")
