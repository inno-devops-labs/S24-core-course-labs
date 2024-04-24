import datetime
import unittest

import pytz
from app import create_app

import re

from app.routes.counts import _create_visit

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a test client before each test."""
        self.app = create_app()
        self.app.config['TESTING'] = True  # You can also set this in a separate config
        _create_visit()
        self.client = self.app.test_client()

    def tearDown(self):
        """Tear down any data after each test."""
        pass

    def test_home_page(self):
        """Test the home page route returns a successful response."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Current Time in Moscow', response.data.decode('utf-8'))

    
    def test_health(self):
        response = self.client.get("/health")
        
        assert response.status_code == 200
        assert response.text == '"OK"'
    
    def test_time_format_on_home_page(self):
        """Test the home page for correct time format YYYY-MM-DD HH:MM:SS."""
        response = self.client.get('/')
        # Define a regular expression pattern for the expected time format
        time_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        # Search for the pattern in the response data
        match = re.search(time_pattern, response.data.decode('utf-8'))
        # Assert that a match was found, indicating the time string is present and correctly formatted
        self.assertIsNotNone(match, "The time string in the format YYYY-MM-DD HH:MM:SS was not found on the home page.")
    
    def test_time_zone_correctness(self):
        """Test that the displayed time is in the Moscow time zone."""
        response = self.client.get('/')
        # Assuming the application returns the time in a <span> with id="time"
        time_pattern = r'id="time">(.+?)</span>'
        match = re.search(time_pattern, response.data.decode('utf-8'))
        if match:
            time_str = match.group(1)
            # Parse the time string
            time_displayed = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            # Convert the displayed time to Moscow time zone
            moscow_zone = pytz.timezone('Europe/Moscow')
            time_displayed = pytz.utc.localize(time_displayed).astimezone(moscow_zone)
            # Get the current time in Moscow
            current_time_moscow = datetime.now(moscow_zone)
            # Check if the displayed time is within a reasonable delta (e.g., a few minutes) of the actual Moscow time
            # This accounts for the delay between the request and the response generation
            delta = abs(time_displayed - current_time_moscow)
            self.assertTrue(delta.seconds < 300, "The displayed time is not correctly adjusted to the Moscow time zone.")
    
    def test_content_type(self):
        """Test that the home page response has the correct content type."""
        response = self.client.get('/')
        self.assertIn('text/html', response.content_type)

    def test_404_error_handling(self):
        """Test that a non-existent route provides a 404 error."""
        response = self.client.get('/non-existent-page')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
