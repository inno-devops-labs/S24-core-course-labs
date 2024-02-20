"""Test module"""

from datetime import datetime
import time
from freezegun import freeze_time
import pytest
import pytz
from main import app


@pytest.fixture(scope="module")
def client():
    """Fixture for creating Flask test client"""
    return app.test_client()


@freeze_time("2024-02-20 12:00:00", tz_offset=3)
def test_current_time(client):
    """Checks whether time from server is correct"""
    tz = pytz.timezone("Europe/Moscow")
    actual_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    resp = client.get("/time")

    assert resp.status_code == 200
    assert "time" in resp.json

    returned_time = resp.json["time"]

    assert returned_time == actual_time


def test_current_time_with_sleep(client):
    """Checks whether time from server is incorrect (with sleep 1)"""
    resp = client.get("/time")

    assert resp.status_code == 200
    assert "time" in resp.json

    returned_time = resp.json["time"]
    time.sleep(1)
    tz = pytz.timezone("Europe/Moscow")
    actual_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    assert returned_time != actual_time
