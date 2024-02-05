import unittest
from datetime import datetime
from app import get_time


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


if __name__ == '__main__':
    unittest.main()
