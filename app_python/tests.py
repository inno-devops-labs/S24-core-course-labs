# tests.py

import unittest
from app import app


class TestMoscowTimeApp(unittest.TestCase):

    def setUp(self):
        # Set up a test client
        self.app = app.test_client()

    def test_homepage_status_code(self):
        """Test the status code of the homepage."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        """Test the content of the homepage."""
        response = self.app.get('/')
        self.assertIn(b"Current Time in Moscow", response.data)
        self.assertIn(b"Date:", response.data)
        self.assertIn(b"Time:", response.data)


if __name__ == '__main__':
    unittest.main()
