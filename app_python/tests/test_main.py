"""Tests for the current Moscow time server."""
from datetime import datetime
import pytz

from app_python.__main__ import get_time  # pylint: disable=E0401


def test_get_time():
    """Ensure the returned time is correct(down to seconds)"""
    dt_got = get_time()
    tz = pytz.timezone("Europe/Moscow")
    dt_actual = datetime.now(tz)

    assert dt_got.replace(microsecond=0) == dt_actual.replace(microsecond=0)
