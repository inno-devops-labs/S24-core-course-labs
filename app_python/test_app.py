import unittest
from datetime import datetime
from app import app
import pytz
import re


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_time(self):
        response = self.app.get('/')
        moscow_tz = pytz.timezone("Europe/Moscow")
        expected_time = datetime.now(moscow_tz).strftime("%d-%m-%Y %H:%M:%S")
        displayed_time = (
            re.search("<h3>(.*)</h3>", response.data.decode('utf-8')).group(1)
        )
        self.assertEqual(displayed_time, expected_time)


if __name__ == '__main__':
    unittest.main()
