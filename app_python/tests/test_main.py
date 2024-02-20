from fastapi.testclient import TestClient
from app.main import app, datetime, moscow_time_zone
import pytest


@pytest.fixture
def client():
    """
    Fixture for creating a test client for the app.
    """
    yield TestClient(app)


def test_api(client):
    """
    Function to test the API with the given client.
    """
    response = client.get("/api/time")
    assert response.status_code == 200
    assert response.json() == {'time': datetime.now(tz=moscow_time_zone).strftime("%H:%M:%S")}
