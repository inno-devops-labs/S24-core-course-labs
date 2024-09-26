import unittest
from time import sleep
from fastapi.testclient import TestClient
import os
import sys
from main import app, get_moscow_time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

client = TestClient(app)


class TimeTest(unittest.TestCase):
    def test_access_to_website(self):
        response = client.get("/")
        assert response.status_code == 200

    def test_correctness_of_time(self):
        response = client.get("/")
        current_time = get_moscow_time()
        assert current_time[0] in response.text and current_time[1] in response.text

    def test_update_of_time_on_refresh(self):
        first_response = client.get("/").text
        sleep(2)
        second_response = client.get("/").text
        self.assertTrue(first_response != second_response)


if __name__ == "__main__":
    unittest.main()
