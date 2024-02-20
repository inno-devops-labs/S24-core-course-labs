from datetime import datetime

import pytest
import pytz

from app.services.time import get_time_in_msk


@pytest.mark.asyncio
async def test_time_is_in_msk():
    time_pre_call = datetime.now(tz=pytz.timezone("Europe/Moscow"))
    time_service_time = await get_time_in_msk()
    time_post_call = datetime.now(tz=pytz.timezone("Europe/Moscow"))
    assert time_pre_call < time_service_time < time_post_call


@pytest.mark.asyncio
async def test_time_changes():
    time_service_time1 = await get_time_in_msk()
    time_service_time2 = await get_time_in_msk()
    assert time_service_time1 < time_service_time2
