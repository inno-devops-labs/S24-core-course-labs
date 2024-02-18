from datetime import datetime, timedelta
from requests import get
import unittest


class TestApp(unittest.TestCase):

    def test_availability(self):
        URL = "http://127.0.0.1:5000"
        assert get(URL, timeout=1).status_code == 200, "Site is not available"

    def test_time(self):
        URL = "http://127.0.0.1:5000"
        msc_time = (datetime.utcnow()
                    + timedelta(hours=3)).strftime("%H:%M:%S")
        assert msc_time in get(URL).text, "Incorrect time"

    def test_index(self):
        URL = "http://127.0.0.1:5000"
        assert "Moscow Time" in get(URL).text, "Index page is not available"


if __name__ == "__main__":
    unittest.main()
