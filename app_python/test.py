import unittest
from unittest.mock import patch
from app import app, get_moscow_time


class TestMoscowTime(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Moscow Time", response.data)
        self.assertIn(b"Current time in Moscow:", response.data)

    def test_get_moscow_time_format(self):
        # Check if the returned time string matches the expected format
        moscow_time = get_moscow_time()
        moscow_time_str = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
        self.assertRegex(moscow_time_str, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

    @patch("app.get_moscow_time")
    def test_index_template_rendering(self, mock_get_moscow_time):
        mock_time = "2024-02-12 12:00:00"
        mock_get_moscow_time.return_value = mock_time
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(mock_time.encode(), response.data)


if __name__ == "__main__":
    unittest.main()

