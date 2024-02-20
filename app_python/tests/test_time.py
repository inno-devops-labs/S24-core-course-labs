import re
from time import sleep
from app.time import get_formatted_moscow_time


def test_get_formatted_moscow_time():
    t1 = get_formatted_moscow_time()
    assert re.match(r"^\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}$", t1) is not None

    sleep(1)
    t2 = get_formatted_moscow_time()
    assert t1 != t2
