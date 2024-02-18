import unittest
from datetime import datetime, timedelta
from app import get_time
import requests


class TestApp(unittest.TestCase):

    def test_time_format(self):
        """
        Test that the time returned by the get_time function is in the expected format.

        This test checks if the time string returned by get_time is in the format
        'YYYY-MM-DD HH:MM:SS', which is the format specified in the get_time function.
        """
        str_time = get_time()
        try:
            # Try to parse the time string in the expected format
            datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            self.fail("Time is not in the expected format")

    def test_time_correctness(self):
        """
        Test the correctness of the time value obtained from the web API and the application.

        This test checks the time retrieved from the WorldTimeAPI for the 'Europe/Moscow' timezone
        against the time obtained from the 'get_time' function in the application. If the time
        difference exceeds two seconds, the test fails.

        Note: Ensure that the application is running, and the WorldTimeAPI is accessible for accurate testing.
        """
        # API link for Moscow timezone
        api_link = 'http://worldtimeapi.org/api/timezone/Europe/Moscow'
        
        # Get time from the WorldTimeAPI
        res = requests.get(api_link)
        api_time = datetime.strptime(res.json()['datetime'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
        
        # Get time from the application
        app_time = datetime.strptime(get_time(), '%Y-%m-%d %H:%M:%S')

        # Check if the time difference exceeds one second
        max_allowed_difference = timedelta(seconds=1)
        if abs(api_time - app_time) >= max_allowed_difference:
            self.fail("Time is not in sync with the Moscow timezone")


if __name__ == '__main__':
    unittest.main()
