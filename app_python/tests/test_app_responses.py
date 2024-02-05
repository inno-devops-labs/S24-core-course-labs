from src.app import app, unify_number
import zoneinfo
from datetime import datetime
from time import sleep


def test_index_status():
    """
    Tests if index response has 'OK' status.
    """
    response = app.test_client().get('/')

    assert response.status_code == 200


def test_index_current_time_in_response():
    """
    Tests if app shows correct time and in correct format in index response.
    """
    response = app.test_client().get('/')

    moscow_tz = zoneinfo.ZoneInfo("Europe/Moscow")
    time_now = datetime.now(moscow_tz)

    hour = unify_number(time_now.hour)
    minute = unify_number(time_now.minute)
    second = unify_number(time_now.second)
    current_time = f"{hour}:{minute}:{second}"

    assert bytes(f"<h1>{current_time}</h1>", "utf-8") in response.data


def test_index_current_date_in_response():
    """
    Tests if app shows correct date and in correct format in index response.
    """
    response = app.test_client().get('/')

    moscow_tz = zoneinfo.ZoneInfo("Europe/Moscow")
    time_now = datetime.now(moscow_tz)

    year = time_now.year
    month = unify_number(time_now.month)
    day = unify_number(time_now.day)
    current_date = f"{year} / {month} / {day}"

    assert bytes(f"<h1>{current_date}</h1>", "utf-8") in response.data


def test_response_updates():
    """
    Tests if time updates after each refresh.
    """
    response1 = app.test_client().get('/')
    sleep(1)
    response2 = app.test_client().get('/')
    sleep(1)
    response3 = app.test_client().get('/')

    time_tag1 = response1.text.split("<h1>")[1]
    time1 = time_tag1.split('</h1>')[0]

    time_tag2 = response2.text.split("<h1>")[1]
    time2 = time_tag2.split('</h1>')[0]

    time_tag3 = response3.text.split("<h1>")[1]
    time3 = time_tag3.split('</h1>')[0]

    assert time1 != time2
    assert time1 != time3
    assert time2 != time3
