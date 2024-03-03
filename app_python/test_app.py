from .app import app, get_moscow_time
import re


def test_get_moscow_time_format():

    moscow_time = get_moscow_time()
    # Check if the returned time matches the format "YYYY.MM.DD HH:MM:SS"
    assert re.match(r"\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}", moscow_time)


def test_home_page():
    """
    Test the home page of the app
    """
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
