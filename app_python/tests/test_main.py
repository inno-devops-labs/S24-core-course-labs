import time

from fastapi.testclient import TestClient

from app_python.main import app

client = TestClient(app)


def test_time_updates():
    """
    Test that the time updates every 5 seconds.
    """
    # Make the first request
    response1 = client.get("/")
    time1 = response1.text

    # Wait for a second to ensure the time changes
    time.sleep(5)  # Wait for at least one second

    # Make the second request
    response2 = client.get("/")
    time2 = response2.text

    # Check if the responses are different
    assert time1 != time2, "The time did not update between requests."
