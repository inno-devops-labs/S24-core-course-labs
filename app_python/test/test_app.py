import datetime
import time

from app.__main__ import app


def test_health():
    """Test 0: Application answers without errors"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_moscow_time_updates():
    """Test 1: If the application response once and one more time after that,
        then the second responses will differ from the first"""
    client = app.test_client()
    first_response = client.get('/')
    first_time = first_response.get_data(as_text=True)

    time.sleep(1)

    second_response = client.get('/')
    second_time = second_response.get_data(as_text=True)

    assert first_time != second_time


def test_moscow_time_go_further():
    """Test 2: If the application response once and one more time after that,
        then the second responses will be more recent time than the first"""
    client = app.test_client()
    first_response = client.get('/')
    first_time = first_response.get_data(as_text=True)
    index_of_time_data = first_time.index("The current time in Moscow is: ") + len("The current time in Moscow is: ")
    first_time = first_time[index_of_time_data:index_of_time_data + 19]

    time.sleep(1)

    second_response = client.get('/')
    second_time = second_response.get_data(as_text=True)
    index_of_time_data = second_time.index("The current time in Moscow is: ") + len("The current time in Moscow is: ")
    second_time = second_time[index_of_time_data:index_of_time_data + 19]

    assert datetime.datetime.fromisoformat(first_time) < datetime.datetime.fromisoformat(second_time)
