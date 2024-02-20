import pytest
import sys
import os
import pytz
from datetime import datetime, timezone
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, get_moscow_time


# Pytest fixture to create a test client for the Flask app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

# Test to check if the home route returns a 200 status code and contains specific text
def test_display_time(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Current Time in Moscow' in response.data

# Test to check if the get_moscow_time function returns the correct Moscow time
def test_get_moscow_time():
    # Assuming your local machine's time zone is UTC
    utc_now = datetime.utcnow()
    moscow_time = get_moscow_time()

    moscow_timezone = pytz.timezone('Europe/Moscow')
    expected_moscow_time = utc_now.replace(tzinfo=timezone.utc).astimezone(moscow_timezone)

    assert moscow_time.strftime('%Y-%m-%d %H:%M:%S') == expected_moscow_time.strftime('%Y-%m-%d %H:%M:%S')

# Test to check the HTML structure and rendering of the time in the template
def test_html_display_time(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Current Time in Moscow' in response.data

    # Ensure the response contains the expected HTML structure
    assert b'<body>' in response.data
    assert b'<p>' in response.data
    assert b'</p>' in response.data
    assert b'</body>' in response.data
    assert b'</html>' in response.data

    # Ensure the time is correctly rendered in the template
    moscow_time = get_moscow_time()
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S').encode('utf-8')
    assert formatted_time in response.data
