import unittest
from flask_testing import TestCase
from datetime import datetime
import pytz
from application import app


class TestApp(TestCase):
    def create_app(self):
        return app

    def test_current_time_displayed(self):
        response = self.client.get('/')
        self.assert200(response)  # Check correct response
        self.assert_template_used('current_time.html')

        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time_str = datetime.now(moscow_tz).strftime('%H:%M:%S')

        # Check that correct time displays on the page
        self.assert_context('current_time', current_time_str)

    def test_main_page_status_code(self):
        # Check 200 code response
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200,
                         "page does not return status 200 OK")

    def test_content_contains_current_time_text(self):
        # page has text "Current Moscow Time"
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn(b"Current Moscow Time", response.data,
                      "Текст 'Current Moscow Time' не найден на странице")


if __name__ == '__main__':
    unittest.main()
