"""Unit tests for main.py"""

from fastapi.testclient import TestClient
from freezegun import freeze_time

from src.main import app

client = TestClient(app)


@freeze_time("2024-02-04T20:19:15+03:00")
def test_read_main():
    """Ensure we can get current time in moscow"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"current_time": "2024-02-04T20:19:15+03:00"}
