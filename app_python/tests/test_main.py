import time
import re

from fastapi.testclient import TestClient

from app_python.main import app

client = TestClient(app)


def test_time_updates():
    """
    Test that the time updates every 5 seconds.
    """
    # Make the first request
    response1 = client.get("/")

    # Extract time from html response
    time1 = response1.text.split("<p>")[1].split("</p>")[0]

    # Wait for a second to ensure the time changes
    time.sleep(5)  # Wait for at least one second

    # Make the second request
    response2 = client.get("/")

    # Extract time from html response
    time2 = response2.text.split("<p>")[1].split("</p>")[0]

    # Check if the responses are different
    assert time1 != time2, "The time did not update between requests."


def test_time_format():
    """
    Test that the time is in the correct format.
    """
    # Make the request
    response = client.get("/")

    # Extract time from html response
    time = response.text.split("<p>")[1].split("</p>")[0]

    # log time in test
    print(time)

    # Check if the time is in the correct format (should match "%H:%M:%S")
    assert re.match(
        r"^\d{2}:\d{2}:\d{2}$",
        time,
    ), "The time is not in the correct format."
