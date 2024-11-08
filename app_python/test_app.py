import unittest
from flask_testing import TestCase
from datetime import datetime, timezone, timedelta
from app import app


class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_current_time_displayed(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('index.html')

        moscow_time = datetime.now(timezone(timedelta(hours=3)))
        current_time_str = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

        self.assert_context('time', current_time_str)

    def test_time_zone_offset(self):
        response = self.client.get('/')
        self.assert200(response)

        displayed_time = self.get_context_variable('time')
        moscow_time = datetime.now(
            timezone(timedelta(hours=3))).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(displayed_time, moscow_time)

    def test_content_contains_date(self):
        response = self.client.get('/')
        today_date = datetime.now(
            timezone(timedelta(hours=3))).strftime('%Y-%m-%d')
        self.assertIn(today_date, response.data.decode())


if __name__ == '__main__':
    unittest.main()
