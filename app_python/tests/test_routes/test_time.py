import datetime
import pytest
import time
from zoneinfo import ZoneInfo


def test_time_response(client):
    response = client.get('/api/v1/time')
    assert response.status_code == 200
    assert 'time' in response.json().keys()


def test_time_correctness(client):
    response = client.get('/api/v1/time')
    current_time = datetime.datetime.combine(datetime.date.today(),
                                             datetime.datetime.now(tz=ZoneInfo("Europe/Moscow")).time())

    got_time = datetime.time.fromisoformat(response.json()['time'])
    got_time_datetime = datetime.datetime.combine(datetime.date.today(), got_time)

    assert current_time - got_time_datetime < datetime.timedelta(seconds=1)


@pytest.mark.usefixtures("instant_sleep")
def test_time_updates(client):
    time_before = datetime.time.fromisoformat(client.get("/api/v1/time").json()['time'])
    time.sleep(secs=9.5)
    time_after = datetime.time.fromisoformat(client.get("/api/v1/time").json()['time'])

    predicted_time_after = (datetime.datetime.combine(datetime.date(1, 1, 1), time_before) + datetime.timedelta(
        seconds=10)).time()

    assert time_after <= predicted_time_after
