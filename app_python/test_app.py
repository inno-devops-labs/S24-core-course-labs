import unittest
import main as app
from datetime import datetime
from datetime import timedelta
import pytz


class AppTest(unittest.TestCase):
    def test_time(self):
        assert (app.get_time(pytz.timezone(app.TIMEZONE)) - datetime.now(pytz.timezone("Europe/Moscow")) <
                timedelta(seconds=1))


    def test_format(self):
        testing_time = app.get_time(pytz.timezone(app.TIMEZONE))
        assert app.format_time(testing_time, app.TIME_FORMAT) == testing_time.strftime("%Y-%m-%d %H:%M:%S")


    def test_workflow(self):
        timezone = pytz.timezone(app.TIMEZONE)
        time = app.get_time(timezone)
        time_string = app.format_time(time, app.TIME_FORMAT)
        assert time_string == datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    unittest.main()