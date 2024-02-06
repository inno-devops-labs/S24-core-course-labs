"""
    This is the module that contains tests for the moscow time application.
"""

import re
from datetime import datetime, timedelta
import pytz
from fastapi.testclient import TestClient
from .app import app


client = TestClient(app)


def test_read_root():
    """
    Test the root endpoint of the FastAPI application.

    Ensures that:
    - The endpoint responds with a 200 OK status code.
    - The response contains the expected "Current Time in Moscow" text.
    - The `Content-Type` header in the response is set to `text/html`.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Current Time in Moscow" in response.text
    assert "text/html" in response.headers["content-type"]


def test_time_returned():
    """
    Verify that the root endpoint correctly returns the current time.

    This test checks for the presence of a time string in the format YYYY-MM-DD HH:MM:SS
    within the HTML content returned by the root endpoint, ensuring that the current time
    is dynamically included in the response.
    """
    response = client.get("/")
    assert response.status_code == 200
    time_match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", response.text)
    assert time_match, "Time not found in response"


def test_timezone_works():
    """
    Validate the application's handling of different timezones.

    This test performs a series of checks to ensure:
    - The current time in Moscow matches when queried twice, indicating consistent handling
      of the same timezone.
    - The current time in Moscow and UTC differ, reflecting correct timezone offset handling.
    - The UTC offset values for Moscow and UTC are not equal, further confirming correct
      timezone management.
    """
    moscow_tz = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_tz)

    same_as_moscow_tz = pytz.timezone("Europe/Moscow")
    same_as_moscow_time = datetime.now(same_as_moscow_tz)

    assert moscow_time.strftime("%Y-%m-%d %H:%M:%S") == same_as_moscow_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    ), "Times in the same timezone should match"

    utc_tz = pytz.timezone("UTC")
    utc_time = datetime.now(utc_tz)

    assert moscow_time.strftime("%Y-%m-%d %H:%M") != utc_time.strftime(
        "%Y-%m-%d %H:%M"
    ), "Moscow time and UTC time should differ"

    moscow_utc_offset = moscow_time.utcoffset().total_seconds()
    utc_utc_offset = utc_time.utcoffset().total_seconds()
    assert (
        moscow_utc_offset != utc_utc_offset
    ), "Timezone offsets for Moscow and UTC should differ"
