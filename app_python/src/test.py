from datetime import timedelta
from time import sleep
from zoneinfo import ZoneInfo

from main import get_current_time


def test_current_time_is_not_too_old():
    time1 = get_current_time()
    assert time1.year >= 2024 and time1.month >= 2 and time1.day >= 19


def test_current_time_is_in_moscow_timezone():
    time1 = get_current_time()
    assert time1.tzinfo == ZoneInfo("Europe/Moscow")


def test_current_time_is_monotonic():
    time1 = get_current_time()
    sleep(0.1)
    time2 = get_current_time()

    assert time1 <= time2
    assert timedelta(seconds=0.1) <= time2 - time1 <= timedelta(seconds=0.2)
