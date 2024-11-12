import requests
import re

_URL = "http://localhost:5000/"

def test_time_server():
    response = requests.get(_URL)

    assert response.status_code == 200
    assert re.search(r"\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2}:\d{2}", response.text)

