import unittest
from datetime import datetime, timedelta

import pytz
from app import app
from bs4 import BeautifulSoup


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_display_time_route_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


def test_display_time_route_current_time(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.data, 'html.parser')

    current_time_tag = soup.find('p')

    self.assertIsNotNone(current_time_tag, "Could not find any <p> tag in the HTML response.")

    current_time_str = current_time_tag.text.strip()

    current_time = datetime.strptime(current_time_str, '%Y-%m-%d %H:%M:%S')

    expected_time = datetime.now(pytz.timezone('Europe/Moscow')).replace(tzinfo=None)

    self.assertAlmostEqual(current_time, expected_time, delta=timedelta(seconds=1))


if __name__ == '__main__':
    unittest.main()
