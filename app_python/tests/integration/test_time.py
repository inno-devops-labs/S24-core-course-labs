import time

from tests.integration.config import client


def test_get_moscow_time_ok():
    response = client.get("/")

    assert response.status_code == 200


def test_get_moscow_time_changes():
    response_1 = client.get("/")
    response_1_text = response_1.text

    time.sleep(1)

    response_2 = client.get("/")
    response_2_text = response_2.text

    assert response_1_text != response_2_text
