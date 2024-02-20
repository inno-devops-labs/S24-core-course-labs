from datetime import datetime

import pytest
import pytz
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.mark.parametrize("path", ["/"])
def test_msc_time_root(path):
    response = client.get(path)
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert "Current Time" in response.text


def test_msc_timezone():
    response = client.get("/")
    moscow_timezone = pytz.timezone("Europe/Moscow")
    current_time_moscow = datetime.now(moscow_timezone)
    current_time_moscow_str = current_time_moscow.strftime("%H:%M:%S %Y-%m-%d")
    assert current_time_moscow_str.encode() in response.content


def test_msc_time_invalid_path():
    response = client.get("/invalid-path")
    assert response.status_code == 404


def test_msc_time_post():
    response = client.post("/")
    assert response.status_code == 405
