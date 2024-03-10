import time
from datetime import datetime

import pytz
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_time_is_equal():
    """
    Check that the time returned by the API is the same as the time on the
    server.
    """
    response = client.get("/")
    assert response.status_code == 200

    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

    # The time returned by the API should be the same
    api_time = response.json()["current_time"]
    assert moscow_time == api_time


def test_time_have_changed():
    """
    Check that the time returned by the API has changed after 1 second.
    """
    response1 = client.get("/")
    assert response1.status_code == 200

    time.sleep(1)

    response2 = client.get("/")
    assert response2.status_code == 200

    assert response1.json()["current_time"] != response2.json()["current_time"]
