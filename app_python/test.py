import unittest
from app import app
import pytz
from datetime import datetime


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_display_moscow_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time_moscow = datetime.now(moscow_tz)
        formatted_time = current_time_moscow.strftime('%Y-%m-%d %H:%M:%S %Z')
        expected_response = f"Current time in Moscow: {formatted_time}"
        self.assertEqual(response.data.decode('utf-8'), expected_response)

    def test_invalid_route(self):
        response = self.app.get('/invalid_route')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
