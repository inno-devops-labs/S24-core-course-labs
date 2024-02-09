from ..server import server
import re
from fastapi.testclient import TestClient
from fastapi.responses import HTMLResponse

client = TestClient(server)

def test_root():
    response: HTMLResponse = client.get("/")
    assert response.status_code == 200

def test_time():
    response = client.get("/time")
    assert response.status_code == 200
    data = response.json()
    assert 'time' in data.keys(), "No time field"
    assert re.match(r'[0-2][0-9]:[0-5][0-9]:[0-5][0-9]', data['time']), "Invalid time format"