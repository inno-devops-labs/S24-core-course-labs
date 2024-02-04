import unittest
import re
from app_python.app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_time_display(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        time_string_regex = r'\d{2}:\d{2}:\d{2}'
        self.assertTrue(re.search(time_string_regex, str(response.data)))


if __name__ == '__main__':
    unittest.main()
