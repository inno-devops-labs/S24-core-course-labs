import unittest
from datetime import datetime, timedelta
from time import sleep
from app import get_time
import pytz


class TestApp(unittest.TestCase):

    def test_time_format(self):
        """
        Test that the time returned by the get_time function is in the expected format.
        """
        str_time = get_time()
        self.assertRegex(str_time, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', "Time is not in the expected format")

    def test_time_correctness(self):
        """
        Test the correctness of the time value obtained from the system and the application.
        """
        app_time = get_time()
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')

        self.assertEqual(app_time, moscow_time, 'Time is not in sync with the Moscow timezone')
    
    def test_(self):
        """
        Test that the time difference between two requests is equal to the specified duration.
        """
        delay_in_seconds = 3

        time_1 = datetime.strptime(get_time(), '%Y-%m-%d %H:%M:%S')
        sleep(delay_in_seconds)
        time_2 = datetime.strptime(get_time(), '%Y-%m-%d %H:%M:%S')

        self.assertEqual(time_2 - time_1, timedelta(seconds=delay_in_seconds), f"The time difference is not equal to {delay_in_seconds}")


if __name__ == '__main__':
    unittest.main()
