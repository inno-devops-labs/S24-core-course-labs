import unittest
from datetime import datetime
from app import app

class FlaskAppTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Initialize the test client for the Flask app
        app.config['TESTING'] = True
        cls.client = app.test_client()
    
    def test_home_status_code(self):
        """Test that the home page loads successfully with status code 200."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, "Home page did not return status code 200")
    
    def test_home_content(self):
        """Test that the home page contains the current time in Moscow."""
        response = self.client.get('/')
        self.assertIn(b'Current Time in Moscow', response.data, "Home page does not contain the expected title")
        
        # Check if the response contains the current time
        # Get current time in Moscow timezone, format it as per the app
        moscow_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertIn(moscow_time.encode(), response.data, "Home page does not contain the expected time")
    
    def test_moscow_image_display(self):
        """Test that the home page contains the Moscow image."""
        response = self.client.get('/')
        self.assertIn(b'<img src="/static/moscow.jpg"', response.data, "Moscow image is not displayed on the home page")

    def test_static_image_access(self):
        """Test that the static Moscow image is accessible directly."""
        response = self.client.get('/static/moscow.jpg')
        self.assertEqual(response.status_code, 200, "Static Moscow image is not accessible")
        self.assertEqual(response.content_type, 'image/jpeg', "Moscow image is not of type 'image/jpeg'")
    
    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        cls.client = None

if __name__ == "__main__":
    unittest.main()