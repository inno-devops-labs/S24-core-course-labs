import pytest
from app import app
from freezegun import freeze_time


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@freeze_time('2024-02-06T11:35:50Z')
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'time_in_moscow' in response.data
    assert response.json['time_in_moscow'] == '2024-02-06 14:35:50'
