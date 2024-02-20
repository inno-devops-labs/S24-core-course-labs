import unittest
from app import app
from datetime import datetime
import pytz

class TestShowTimeFunction(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_time_format(self):
        response = self.app.get('/')
        moscow_timezone = pytz.timezone('Europe/Moscow')
        time_now = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
        self.assertIn(time_now, response.get_data(as_text=True))

    def test_time_correctness(self):
        response = self.app.get('/')
        moscow_timezone = pytz.timezone('Europe/Moscow')
        time_now = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
        expected_html = f'<strong>{time_now}</strong>'
        self.assertIn(expected_html, response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
