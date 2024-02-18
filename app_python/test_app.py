import unittest
from app import app
from datetime import datetime
import pytz


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_page_moscow_time(self):
        result = self.app.get('/')
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
        self.assertIn(moscow_time, result.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
