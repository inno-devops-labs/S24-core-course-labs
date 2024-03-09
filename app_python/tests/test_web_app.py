import re
from datetime import timedelta
from time import sleep

from pytest import fixture

from moscow_time import app


app.config.update({
    "TESTING": True,
})
client = app.test_client()


def hms(hours: int, minutes: int, seconds: int) -> timedelta:
    return timedelta(hours=hours, minutes=minutes, seconds=seconds)


def test_get_index():
    resp1 = client.get('/')
    sleep(1)
    resp2 = client.get('/')

    assert resp1.status_code == 200
    assert resp2.status_code == 200

    pattern = re.compile(br'(\d{1,2}):(\d{1,2}):(\d{1,2})')

    data1 = pattern.search(resp1.data)
    data2 = pattern.search(resp2.data)
    assert data1, "Time is in the response"
    assert data2, "Time is in the second response"

    time1 = hms(*map(int, data1.groups()))
    time2 = hms(*map(int, data2.groups()))

    # Time difference is positive but no more than 2 seconds
    assert timedelta(0) < time2 - time1 <= timedelta(seconds=2)

def test_wrong_url():
    resp = client.get('/arbitrary/url')
    assert resp.status_code == 404

def test_post_index():
    resp = client.post('/')
    assert resp.status_code == 405
