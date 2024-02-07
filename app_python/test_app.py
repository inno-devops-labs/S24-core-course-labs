import requests
import pytest
from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_read_time():
    response = client.get("/current_time")
    assert response.status_code == 200
    assert "Current Moscow Time" in response.json()

