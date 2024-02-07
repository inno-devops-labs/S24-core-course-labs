import pytest
import time
from bs4 import BeautifulSoup
from app_python.flaskr.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_response(client):
    # test whether request is successful
    response = client.get('/')
    assert response.status_code == 200


def test_existance_of_time(client):
    # test whether there exists time in the response data
    response = client.get('/')
    assert response.status_code == 200
    assert b'MSK Time' in response.data


def test_subsequent_requests(client):
    # test whether two subsequent requests get different times
    response1 = client.get('/')
    time.sleep(2)
    response2 = client.get('/')

    assert response1.status_code == 200
    assert response2.status_code == 200

    soup1 = BeautifulSoup(response1.data, 'html.parser')
    soup2 = BeautifulSoup(response2.data, 'html.parser')

    time_node1 = soup1.find_all("p")
    time_node2 = soup2.find_all("p")

    assert time_node1 is not None
    assert time_node2 is not None

    assert len(time_node1) == 1
    assert len(time_node2) == 1

    time_node1 = time_node1[0]
    time_node2 = time_node2[0]

    assert time_node1.get_text(strip=True) != time_node2.get_text(strip=True)
