from fastapi.testclient import TestClient
from app import app
import pytest
from datetime import datetime
from pytz import timezone

client = TestClient(app)


def test_read_root():
    response = client.get("/current_time")
    assert response.status_code == 200

    moscow_tz = timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    expected_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')

    current_time = response.json()["Current Moscow Time"]
    assert current_time[:19] == expected_time[:19]
    assert current_time[19:] == expected_time[19:]


def test_root_path():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


if __name__ == "main":
    pytest.main()
