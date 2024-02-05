import unittest
from flask import Flask
from app.routes import get_moscow_time
from datetime import datetime, timedelta
import pytz

class FlaskAppTest(unittest.TestCase):
    """
    A unit test class for the Flask application.
    """
    def setUp(self):
        """
        Set up a test Flask application.
        """
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    def test_get_moscow_time(self):
        """
        Raises:
            AssertionError: If the time difference exceeds the threshold (5 seconds).
        """
        current_time_utc = datetime.utcnow()

        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time_moscow = current_time_utc.replace(tzinfo=pytz.utc).astimezone(moscow_tz)

        moscow_time_str = get_moscow_time()
        moscow_time = datetime.strptime(moscow_time_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=moscow_tz)

        time_difference = current_time_moscow - moscow_time
        threshold = timedelta(seconds=5)

        self.assertLessEqual(time_difference, threshold)

if __name__ == '__main__':
    unittest.main()
