import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Current Time in Moscow</title>', response.data)
        self.assertIn(b'The current time in Moscow is:', response.data)


if __name__ == '__main__':
    unittest.main()
