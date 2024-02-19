import datetime
import unittest
import pytz
from app import msk_timezone


class TestApp(unittest.TestCase):
    def test_msk_timezone(self):
        resultTimeStr = msk_timezone()
        time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        timeStr = time.strftime("Current time (MSK timezone): %H:%M:%S")
        self.assertLessEqual(resultTimeStr, timeStr)


if __name__ == "__main__":
    unittest.main()
