import unittest
import time
from app import app

class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Time in Moscow:', response.data)

    def test_time_updates(self):
        response1 = self.app.get('/')
        time.sleep(1)
        response2 = self.app.get('/')
        self.assertNotEqual(response1.data, response2.data)

if __name__ == '__main__':
    unittest.main()