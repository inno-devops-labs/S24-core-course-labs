import unittest
from flask import Flask
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

if __name__ == '__main__':
    unittest.main()
