from fastapi.testclient import TestClient
import time
from ...main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")

    assert response.status_code == 200

    moscow_time_prev = response.text.split("<h2>")[1].split("</h2>")[0]

    assert "Current Moscow Time" in response.text

    # get new time after 1 second
    time.sleep(1)
    new_response = client.get("/")

    assert new_response.status_code == 200

    moscow_time_new = new_response.text.split("<h2>")[1].split("</h2>")[0]

    assert moscow_time_prev != moscow_time_new
    assert "Current Moscow Time" in response.text
