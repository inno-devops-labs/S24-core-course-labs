import unittest
from datetime import datetime
import pytz
from time_zone import msk_time


class TestMoscowTime(unittest.TestCase):
    def test_get_moscow_time_format(self):
        moscow_time = msk_time()
        self.assertRegex(
            moscow_time, r'\d{2}:\d{2}:\d{2}')

    def test_msk_timezone(self):
        time = datetime.now(pytz.timezone('Europe/Moscow'))
        self.assertLessEqual(msk_time(), time.strftime(
            "Current time (MSK timezone): %H:%M:%S"))


if __name__ == '__main__':
    unittest.main()
