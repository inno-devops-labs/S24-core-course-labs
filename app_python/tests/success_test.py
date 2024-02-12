from time import sleep
import pytest

from app_python.app.server import app


@pytest.fixture
def fixture():
    return app


def test_request_successful(fixture):
    """
    A test for successful request
    """
    request, response = fixture.test_client.get()

    assert request.method.lower() == "get"
    assert response.status == 200


def test_content_change(fixture):
    """
    A test for changing body
    """
    first_request, first_response = fixture.test_client.get()
    sleep(1)
    second_request, second_response = fixture.test_client.get()

    assert first_response.status == 200
    assert second_response.status == 200
    assert first_response.body != second_response.body
