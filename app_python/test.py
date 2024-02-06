import unittest
from app import app
import datetime
import time

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_display_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime('%d.%m.%y %H:%M:%S'), 'utf-8'), response.data)
        time.sleep(2)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime('%d.%m.%y %H:%M:%S'), 'utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()