"""
Web app unit tests
"""

from datetime import datetime, timezone, timedelta
from flask.testing import FlaskClient


def test_availability(client: FlaskClient) -> None:
    """
    Pytest test availability
    """
    response = client.get("/")
    assert response.status_code == 200


def test_html(client: FlaskClient) -> None:
    """
    Pytest test HTML contents
    """
    response = client.get("/").text
    assert "Moscow" in response, "Html is broken"


def test_time(client: FlaskClient) -> None:
    """
    Pytest test Moscow time for correctness
    """
    response = client.get("/").text

    zone = timezone(timedelta(hours=3))
    time = datetime.now(timezone.utc).astimezone(zone)

    # Ignore milliseconds because of tests framework & requests overhead
    time_wo_ms = str(time).split(".", maxsplit=1)[0]

    assert time_wo_ms in response, "Time is broken"
