import time
import datetime
import pytest
from requests import get


@pytest.mark.usefixtures("instant_sleep")
def test_time_refreshing():
    time_before = datetime.time.fromisoformat(get("http://localhost:5000/api/v1/time").json()['time'])
    time.sleep(secs=9.5)
    time_after = datetime.time.fromisoformat(get("http://localhost:5000/api/v1/time").json()['time'])

    predicted_time_after = (datetime.datetime.combine(datetime.date(1, 1, 1), time_before) + datetime.timedelta(
        seconds=10)).time()

    assert time_after <= predicted_time_after
