import unittest
from app import create_app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a test client before each test."""
        self.app = create_app()
        self.app.config['TESTING'] = True  # You can also set this in a separate config
        self.client = self.app.test_client()

    def tearDown(self):
        """Tear down any data after each test."""
        pass

    def test_home_page(self):
        """Test the home page route returns a successful response."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Current Time in Moscow', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
