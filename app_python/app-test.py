import unittest
from app import app
class AppTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_display_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Current time in Moscow' in response.data)

if __name__ == '__main__':
    unittest.main()