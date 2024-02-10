"""
This file contains the unit tests for the app_utils.py file.
"""

import unittest
from app_python.app_utils import return_tz_time, return_time


class TestAppUtils(unittest.TestCase):
    """
    Test cases for the app_utils.py file.
    """

    def test_return_tz_time(self):
        """
        Tests the return_tz_time function.
        It checks for different timezones and compares the results.
        """
        # Istanbul and Moscow time will be same if return_tz_time is working correctly
        self.assertEqual(
            return_tz_time("Europe/Istanbul"), return_tz_time("Europe/Moscow")
        )
        # Tokyo and Moscow time will be different for the same reason
        self.assertNotEqual(
            return_tz_time("Asia/Tokyo"), return_tz_time("Europe/Moscow")
        )

    def test_return_time(self):
        """
        Tests the return_time function.
        It checks if the current Moscow time is in the current time string.
        """
        self.assertIn(return_tz_time("Europe/Moscow"), return_time())
