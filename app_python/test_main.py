import time
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from main import app
from freezegun import freeze_time
import pytz


@pytest.fixture(scope="module")
def test_client():
    """Fixture for creating a FastAPI test client."""
    return TestClient(app)


@freeze_time("2024-02-04 12:00:00", tz_offset=3)
def test_get_current_time_returns_correct_time(test_client):
    """Test that the endpoint returns the current time in Moscow timezone."""

    # Act
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")
    response = test_client.get("/")

    # Assert
    assert response.status_code == 200
    assert "time" in response.json()

    # Get the time from the response JSON
    returned_time_str = response.json()["time"]

    # Ensure the returned time matches the frozen time
    assert returned_time_str == current_time


def test_get_current_time_returns_correct_time_with_sleep(test_client):
    """
    Times must be different, because we will sleep 1 second.
    """

    # Act
    response = test_client.get("/")

    # Assert
    assert response.status_code == 200
    assert "time" in response.json()

    # Sleep and get time
    time.sleep(1)
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz).strftime("%Y-%m-%d %H:%M:%S")

    # Get the time from the response JSON
    returned_time_str = response.json()["time"]

    # Ensure the returned time matches the frozen time
    assert returned_time_str != current_time
