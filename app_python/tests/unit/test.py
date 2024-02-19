# test_app.py
from fastapi.testclient import TestClient
from app_python.main import app
from datetime import datetime, timedelta
import pytz
import re

client = TestClient(app)


def test_response_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_moscow_time():
    delta = timedelta(seconds=1)

    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_current_time = datetime.now(moscow_tz)

    response = client.get("/")

    date_string = re.search(
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", response.text
    ).group()
    date_result = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    date_result = moscow_tz.localize(date_result)

    assert abs(date_result - moscow_current_time) < delta


def test_invalid_endpoint():
    response = client.get("/invalid_endpoint")
    assert response.status_code == 404
