from datetime import datetime

from src.business_logic import get_current_moscow_time, get_human_readable_time


def test_get_current_moscow_time():
    dt = get_current_moscow_time()

    assert (
            type(dt) is datetime
    ), "Function `get_current_moscow_time` does not return a `datetime` object"


def test_get_human_readable_time():
    dt = get_current_moscow_time()

    weekday = dt.strftime("%a")
    month = dt.strftime("%b")
    day = dt.strftime("%d")
    year = dt.strftime("%Y")
    hour = dt.strftime("%H")
    minute = dt.strftime("%M")
    second = dt.strftime("%S")

    human_readable_time = f"{weekday}, {month} {day} {year},"\
                          f" {hour}:{minute}:{second}"

    assert human_readable_time == get_human_readable_time(
        dt
    ), "Convertion to human readable time did not succeed"
