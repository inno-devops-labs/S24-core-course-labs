import re
import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_display_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Time in Moscow:', response.data)

    def test_time_format(self):
        response = self.app.get('/')
        time_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
        self.assertTrue(time_pattern.search(response.get_data(as_text=True)))


if __name__ == '__main__':
    unittest.main()