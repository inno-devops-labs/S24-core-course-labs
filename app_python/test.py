import datetime
import re
import zoneinfo

import pytest
from main import app


@pytest.fixture()
def app_testing():
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app_testing):
    return app_testing.test_client()


isotime_regex = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}T"
                           "[0-9]{2}:[0-9]{2}:[0-9]{2}\\.[0-9]{6}\\+03:00")


def test_index_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers.get("Content-Type") == "text/html; charset=utf-8"
    assert len(response.data) == 32
    assert isotime_regex.match(response.data.decode("utf-8")) is not None


@pytest.fixture()
def index_time(client):
    response = client.get("/")
    return response.data.decode("utf-8")


def test_time_valid(index_time):
    b = datetime.datetime.fromisoformat(index_time)
    assert b is not None
    assert b.tzname() == "UTC+03:00"
    a = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Moscow"))
    delt = a - b
    assert delt < datetime.timedelta(milliseconds=10)
