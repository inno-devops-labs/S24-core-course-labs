"""
This module contains the unit tests for the
Flask application that displays the current time in Moscow.А
"""
import datetime
import pytest
from app import app


@pytest.fixture
def client():
    """
    This fixture returns a test client for the Flask application.
    """
    app.config['TESTING'] = True
    with app.test_client() as web_client:
        yield web_client


def test_display_time():
    """
    This test checks if the current time in Moscow is displayed correctly.
    """
    app.config['TESTING'] = True
    with app.test_client() as web_client:
        response = web_client.get('/')
        assert b'The current time in Moscow: ' in response.data
        moscow_time = datetime.datetime.now(datetime.timezone.utc).astimezone(
            datetime.timezone(datetime.timedelta(hours=3)))
        assert moscow_time.strftime("%H:%M:%S").encode() in response.data


def test_display_time_changes():
    """
    This test checks if the current time in Moscow
    changes after refreshing the page
    """
    app.config['TESTING'] = True
    with app.test_client() as web_client:
        response = web_client.get('/')
        assert b'The current time in Moscow: ' in response.data
        moscow_time = datetime.datetime.now(datetime.timezone.utc).astimezone(
            datetime.timezone(datetime.timedelta(hours=3)))
        assert moscow_time.strftime("%H:%M:%S").encode() in response.data
        response = web_client.get('/')
        assert b'The current time in Moscow: ' in response.data
        moscow_time2 = datetime.datetime.now(datetime.timezone.utc).astimezone(
            datetime.timezone(datetime.timedelta(hours=3)))
        assert moscow_time2.strftime("%H:%M:%S").encode() in response.data
        assert moscow_time != moscow_time2


if __name__ == '__main__':
    pytest.main()
