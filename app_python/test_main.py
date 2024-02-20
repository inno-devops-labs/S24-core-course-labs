import time

from fastapi.testclient import TestClient

from main import app

test_client = TestClient(app)


def test_time_changes():
    # Checks if the content of the response changes after a delay.
    response_a = test_client.get('/')
    time.sleep(1)
    response_b = test_client.get('/')
    # if responses are not equal the time has changed
    assert response_a.content != response_b.content


def test_main200():
    # Checks if the status code of the main endpoint is 200.
    response = test_client.get('/')
    assert response.status_code == 200


def test_nonexistent404():
    # Checks if the status code of a non-existing path is 404.
    response = test_client.get('/non-existing-path')
    assert response.status_code == 404
