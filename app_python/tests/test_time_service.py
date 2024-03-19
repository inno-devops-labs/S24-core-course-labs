import unittest
from datetime import timedelta

from app_python.services.time_service import TimeService


class TestTimeService(unittest.TestCase):
    def test_new_york_time_ahead_of_moscow_time(self):
        new_york_datetime = TimeService(timezone_str='America/New_York').get_current_datetime()
        moscow_datetime = TimeService(timezone_str='Europe/Moscow').get_current_datetime()

        self.assertEqual((new_york_datetime + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'),
                         moscow_datetime.strftime('%Y-%m-%d %H:%M:%S'))

    def test_get_current_time_different_timezones(self):
        datetime1 = TimeService(timezone_str='America/New_York').get_current_time_str()
        datetime2 = TimeService(timezone_str='Europe/London').get_current_time_str()

        self.assertNotEqual(datetime1, datetime2)


if __name__ == '__main__':
    unittest.main()
