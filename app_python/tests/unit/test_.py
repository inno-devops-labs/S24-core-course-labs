"""
Tests for main.py
"""

import os
import sys
import time

import pytest

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..")
)
sys.path.insert(0, project_root)

from app_python.src.main import app


@pytest.fixture
def client():
    """Create a test client for app"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_app(client):
    """Test that the response is successful"""
    response = client.get("/")
    assert response.status_code == 200


def test_time(client):
    """Test that time increase"""
    time_1 = client.get("/").data
    print(time_1)
    time.sleep(1)

    assert time_1 < client.get("/").data
