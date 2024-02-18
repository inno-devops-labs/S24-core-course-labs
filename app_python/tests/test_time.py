import pytz
import json
from app.main import get_timestamp, format_datetime_response
from datetime import datetime


def test_get_timestamp_type():
    assert type(get_timestamp()) is datetime


def test_get_timestamp_validity():
    tz_name = "Europe/Moscow"
    tz = pytz.timezone(tz_name)
    timestamp = tz.localize(datetime.now(), is_dst=None)
    assert abs(get_timestamp().timestamp() - timestamp.timestamp()) < 1


def test_get_timestamp_timezone():
    tz_name = "Europe/Moscow"
    tz = pytz.timezone(tz_name)
    assert get_timestamp().tzname() == tz.tzname(datetime.now())


def test_response_formatting():
    dt = datetime.now()
    formatted_response = format_datetime_response(dt)
    assert type(formatted_response) is str
    assert json.loads(formatted_response)
    assert "time" in json.loads(formatted_response).keys()
