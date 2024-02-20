import unittest
from app import app
from datetime import datetime, timedelta
import pytz

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,  200)

        # Check that the time is within the last minute
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
        self.assertTrue(moscow_time in response.data.decode())

if __name__ == '__main__':
    unittest.main()
