import sys
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(__file__) + "/.."))

from app_python.app import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_display_time(client):
    response = client.get('/')
    assert b'Current Date And Time in Moscow:' in response.data
