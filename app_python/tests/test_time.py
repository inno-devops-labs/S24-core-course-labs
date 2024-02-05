from app_python.src.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_time():
    response = client.get("/moscow-time")

    assert response.status_code == 200
