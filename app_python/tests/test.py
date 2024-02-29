import unittest

import pytz
from app_python.app import get_time_with_tz
from datetime import datetime


class TestFlaskApp(unittest.TestCase):
    def test_get_time(self):
        tz = "Europe/Moscow"
        format = "%Y-%m-%d %H:%M:%S"
        expected = datetime.now(pytz.timezone(tz)).strftime(format)
        self.assertEqual(get_time_with_tz(tz), expected)


if __name__ == "__main__":
    unittest.main()
