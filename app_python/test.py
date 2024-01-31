import unittest
from app import get_moscow_time


class TestMoscowTime(unittest.TestCase):
    def test_get_moscow_time_format(self):
        # Check if the returned time string matches the expected format
        moscow_time = get_moscow_time()
        moscow_time_str = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
        self.assertRegex(moscow_time_str, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')


if __name__ == '__main__':
    unittest.main()

