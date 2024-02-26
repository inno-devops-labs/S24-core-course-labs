import time
import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_check_status(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_get_moscow_time(self):
        response1 = self.app.get('/')
        time.sleep(1)
        response2 = self.app.get('/')
        self.assertNotEqual(response1.data, response2.data)


if __name__ == '__main__':
    unittest.main()
