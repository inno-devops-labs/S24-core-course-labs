import pytest
from ..app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Current Time' in response.data


def test_current_time_format(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<p>' in response.data  # Assuming the time is wrapped in a <p> tag
