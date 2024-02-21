import unittest
from app_python.app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_display_time(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Check if the response contains the expected text format
        self.assertIn(b'Current time in the city:', response.data)
        # You may also check for the datetime format
        self.assertRegex(response.data.decode(), r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

if __name__ == '__main__':
    unittest.main()
