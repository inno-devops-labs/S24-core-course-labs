import datetime
from app_python.api.services.moscow_time import get_current_moscow_time


def test_get_current_moscow_time():
    cur_time = get_current_moscow_time()
    assert cur_time.tzname == "Europe/Moscow"
    assert (cur_time - datetime.datetime.now()).total_seconds() < 1
