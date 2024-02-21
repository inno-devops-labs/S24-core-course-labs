import pytest
from app import app
from datetime import datetime
import pytz

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_time(client):
    response = client.get('/')
    assert response.status_code == 200  # Check if the request was successful
    assert b'The current time in Moscow is:' in response.data  # Check for the presence of the message

    # Validate the format of the time returned in the response
    moscow = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S').encode()
    assert moscow_time in response.data
