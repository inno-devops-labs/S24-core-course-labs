"""
This module contains the unit tests for the Moscow time endpoint.
"""
import re
import unittest
import time

from app_python.app import app


class MoscowTimeTestCase(unittest.TestCase):
    """
    Unit tests for the Moscow time endpoint.
    """

    def setUp(self):
        """
        Setting up the app for testing
        :return:
        """
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_time_changes(self):
        """
        Test that the time changes
        """
        # Getting the time
        response = self.app.get("/show_moscow_time")
        time_match = re.search(r'\d{2}:\d{2}:\d{2}', response.get_data(as_text=True))
        if time_match:
            first_time = time_match.group()
        else:
            assert False, "Couldn't parse time from response"

        # Wait to ensure time is changed
        time.sleep(1)

        # Getting the time again
        response = self.app.get("/show_moscow_time")
        time_match = re.search(r'\d{2}:\d{2}:\d{2}', response.get_data(as_text=True))
        if time_match:
            second_time = time_match.group()
        else:
            assert False, "Couldn't parse time from response"

        # Checking that results are different
        assert first_time != second_time, "Time should change between requests!"


if __name__ == "__main__":
    unittest.main()
