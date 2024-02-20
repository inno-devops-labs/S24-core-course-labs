import pytest
from app_python.app import app
import re


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_current_time_format(client):
    response = client.get("/")
    data = response.get_data(as_text=True)
    assert response.status_code == 200
    assert re.match(
        r"The current time in Moscow is: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
        data,
    )
    
