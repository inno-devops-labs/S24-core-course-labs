import datetime

import pytest
import pytz
from app.domain.time import TimeManager

DATETIME_FRACTIONS = ["year", "month", "day", "hour", "minute", "second"]


@pytest.mark.asyncio
async def test_current_time_moscow(time_manager_factory):
    time_manager: TimeManager = await time_manager_factory()
    curr_datetime = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow"))

    _datetime = await time_manager.datetime()

    for part in DATETIME_FRACTIONS:
        assert getattr(curr_datetime, part) == getattr(_datetime, part)
