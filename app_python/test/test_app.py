import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from datetime import datetime, timezone, timedelta
from app import app, get_moscow_time
import time

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_moscow_time(self):
        """Test if get_moscow_time returns the current time."""
        moscow_time = get_moscow_time()
        current_time = datetime.now(timezone.utc) + timedelta(hours=3)
        self.assertEqual(moscow_time, current_time.strftime('%Y-%m-%d %H:%M:%S'))

    def test_index_route(self):
        """Test if index route returns the current time."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_correct_html(self):
        """Test if defined text is displayed on web page"""
        response = self.app.get('/')
        self.assertIn(b'Current Time in Moscow', response.data)

    def test_download_speed(self):
        """Test if download speed is enough (very fast)"""
        start = time.time()
        response = self.app.get('/')
        end = time.time()
        self.assertLess(end - start, 0.1)




if __name__ == '__main__':
    unittest.main()
