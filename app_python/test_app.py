import time
import pytest
from app import app
from freezegun import freeze_time


@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client


@freeze_time('2024-02-06T11:35:50Z')
def test_get_fixed_time(client):
    response = client.get('/')

    # test correct response
    assert response.status_code == 200

    # test correct timezone
    assert b'time_in_moscow' in response.data

    # test correct time in moscow timezone
    assert response.json['time_in_moscow'] == '2024-02-06 14:35:50'


def test_get_time_after_sleep(client):
    response = client.get('/')

    # test correct response
    assert response.status_code == 200

    # test correct timezone
    assert b'time_in_moscow' in response.data

    time.sleep(2)
    cur_time = client.get('/').json['time_in_moscow']

    # test different time
    assert response.json['time_in_moscow'] != cur_time
