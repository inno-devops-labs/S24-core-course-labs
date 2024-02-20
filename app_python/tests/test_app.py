"""
Unit Tests Documentation for Flask Web App

This module contains unit tests for the functions and routes implemented in the
Flask web app that displays the current time in Moscow. The tests are designed
 to verify the correctness and functionality of the app's core features.

Requirements:
    - Flask: Ensure Flask is installed (pip install Flask)
    - pytz: Ensure pytz is installed (pip install pytz)

Note:
    - These tests assume that the Flask app is running correctly and the
    HTML template is properly set up.
    - It's recommended to run the tests in a controlled environment, as they
     may interact with external dependencies such as the current time and
      Flask routes.

"""

import unittest
from app import app, get_moscow_time, formatted_time
from datetime import datetime
import pytz

# Constants used in tests
TIMESTAMP_CONSTANT = 1672138646.118119
TIMEZONE_STRING = 'Europe/Moscow'
FORMAT_STRING = '%Y-%m-%d %H:%M:%S'


class TestApp(unittest.TestCase):
    """
    Test Cases for Flask Web App Functionality

    This class contains individual test methods to validate specific
     functionalities of the Flask web app.
    """

    def setUp(self):
        """
        Test Setup Method

        Initializes resources required for testing, such as the Flask app
         client.
        """
        self.app = app.test_client()

    def test_time_accuracy(self):
        """
        Test Time Accuracy

        Verify the accuracy of the time retrieved by the get_moscow_time
        function against the actual time in the Europe/Moscow timezone.
        """
        # Get time from the app's function
        time = get_moscow_time()
        # Get the current time in UTC
        utc_now = datetime.utcnow()

        # Set the timezone to Moscow
        moscow_tz = pytz.timezone(TIMEZONE_STRING)
        correct_time = utc_now.replace(tzinfo=pytz.utc).astimezone(moscow_tz)

        # Assert that the received time is synchronized with the
        # Europe/Moscow timezone
        self.assertAlmostEqual(time.timestamp(), correct_time.timestamp(), 0,
                               'The received time is not synchronized with '
                               'the Europe/Moscow timezone.')

    def test_time_format(self):
        """
        Test Time Format

        Validate the format of the time string returned by the formatted_time
         function.
        """
        # Time that will be used for testing
        testing_time = datetime.fromtimestamp(TIMESTAMP_CONSTANT)
        # Conversion to a specific format using tested function
        time = formatted_time(testing_time)
        # Checking format
        correct_format = datetime.strptime(time, FORMAT_STRING)

        # Assert that the received time format is appropriate
        self.assertTrue(correct_format, 'The received time format is not'
                                        ' appropriate')

    def test_display_moscow_time(self):
        """
        Test Display Moscow Time Route

        Ensure that the display_moscow_time route returns a valid response.
        """
        response = self.app.get('/')

        # Assert that the HTTP status code is 200 (OK)
        self.assertEqual(response.status_code, 200, 'The received status code'
                                                    ' is not 200')


if __name__ == 'main':
    unittest.main()
