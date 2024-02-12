import time

from fastapi.testclient import TestClient

from .app import app

client = TestClient(app)

def test_status():
    response = client.get("/")
    assert response.status_code == 200


def test_time_changes():
    resp = client.get("/")
    text1 = resp.text

    time.sleep(3)

    resp = client.get('/')
    text2 = resp.text

    assert text1 != text2