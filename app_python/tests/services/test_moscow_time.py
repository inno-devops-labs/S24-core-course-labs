import datetime

import pytz
from api.services.moscow_time import get_current_moscow_time


def test_get_current_moscow_time():
    cur_time = get_current_moscow_time()
    # assert cur_time.tzname == "Europe/Moscow"
    # print(cur_time.tzname)
    assert (cur_time - datetime.datetime.now(pytz.timezone("Europe/Moscow"))).total_seconds() < 1
