"""
Unit tests for the web application.
"""

import datetime
import pytest

from app import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask application.
    """
    app.config['TESTING'] = True

    with app.test_client() as test_client:
        yield test_client


def test_home():
    """
    Test the home route ("/") of the application.
    """
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Current Time in Moscow' in response.data


def test_home_time(monkeypatch):
    """
    Test the home route ("/") of the application with a mocked time.
    """
    mock_time = datetime.datetime(2024, 1, 1, 12, 0, 0)

    class MockDatetime:
        def now(self, *args):
            return mock_time

    monkeypatch.setattr(datetime, 'datetime', MockDatetime())

    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'2024-01-01 12:00:00' in response.data
