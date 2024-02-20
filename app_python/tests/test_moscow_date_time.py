import unittest
from datetime import datetime
from unittest.mock import patch

import pytz
from app.moscow_date_time import get_moscow_date_time


class TestGetMoscowDateTime(unittest.TestCase):
    @patch('datetime.datetime')
    def test_moscow_time(self, mock_datetime):
        """
        Checks if a `get_moscow_date_time` actually returns `datetime` with
        timezone of `Europe/Moscow`
        """
        mock_datetime.utcnow.return_value = datetime(
            2024, 2, 20, 12, 0, 0, tzinfo=pytz.utc
        )

        moscow_time = get_moscow_date_time()
        print(moscow_time.tzinfo)
        moscow_timezone = moscow_time.tzinfo
        if moscow_timezone is None:
            self.assertFalse(
                moscow_timezone is None, 'Returned timezone is None'
            )
        else:
            self.assertEqual(
                moscow_timezone.tzname(None),
                'Europe/Moscow',
            )


if __name__ == '__main__':
    unittest.main()
