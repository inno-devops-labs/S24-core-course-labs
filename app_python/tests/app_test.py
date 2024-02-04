from datetime import datetime
from requests import get

URL = "http://127.0.0.1:5000"

def test_availability():
    assert get(URL, timeout=1).status_code == 200, "Site is not available"

def test_time():
    assert datetime.now().strftime("%H:%M") in get(URL).text, "Incorrect time"

if __name__ == "__main__":
    test_availability()
    print("Availability test passed")
    test_time()
    print("Time test passed")