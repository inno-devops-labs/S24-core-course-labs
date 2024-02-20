import unittest
from app import app


class TestApp(unittest.TestCase):

    def test_display_time_msk(self):
        with app.test_client() as client:
            response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Current time in Moscow:", response.data)


if __name__ == '__main__':
    unittest.main()
