import datetime

from app_python.app import app as flask_app
from app_python.app import current_time


def test_mentions_moscow():
    response = flask_app.test_client().get('/')

    assert response.status_code == 200
    assert "Moscow" in response.data.decode('utf-8')


def test_time_format():
    assert datetime.datetime.strptime(current_time(), "%H:%M:%S")
