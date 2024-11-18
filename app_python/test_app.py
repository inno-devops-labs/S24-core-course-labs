import pytest
from app import app
from datetime import datetime
import pytz


@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:
        yield client


# Helper function to get current Moscow time in the desired format
def get_moscow_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    return datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')


# Test to ensure the correct Moscow time is returned in the response
def test_show_time(client):
    # Get the expected Moscow time
    expected_time = get_moscow_time()

    # Make a GET request to the root endpoint
    response = client.get('/')

    # Assert that the status code is 200 (OK)
    assert response.status_code == 200, (f"Expected status code 200, but got"
                                         f" {response.status_code}")

    # Assert the response contains the expected
    # Moscow time in the formatted string
    assert f"Moscow Time: {expected_time}" in response.data.decode(), \
        (f"Expected 'Moscow Time: {expected_time}'"
         f" in response, but got {response.data.decode()}")
