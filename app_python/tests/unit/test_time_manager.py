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


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "dump_format", ["%H:%M:%S %d.%m.%Y", "%d.%m.%Y", "%H:%M %d.%m.%Y"]
)
async def test_current_time_str(time_manager_factory, dump_format: str):
    time_manager: TimeManager = await time_manager_factory({"dump_format": dump_format})
    curr_datetime = datetime.datetime.now(tz=pytz.timezone("Europe/Moscow")).strftime(
        dump_format
    )

    str_datetime = await time_manager.str_datetime()

    assert curr_datetime == str_datetime
