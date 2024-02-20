import unittest
import re
from main import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_display_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        time_string_regex = r'\d{2}:\d{2}:\d{2}'
        self.assertTrue(re.search(time_string_regex, str(response.data)))


if __name__ == '__main__':
    unittest.main()
