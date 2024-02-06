"""Test module"""

import unittest
from main import app

class AppTestCase(unittest.TestCase):
    """Unit tests for the get current time endpoints"""
    def setUp(self):
        self.app = app.test_client()

    def test_get_current_time(self):
        """Test for get("/")"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('The current time in Moscow is', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
