import unittest
from datetime import datetime
import pytz
from app_python import main


class TestApp(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.client = main.app.test_client()

    def test_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_time_format(self):
        response = self.client.get('/')
        msk_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('Current time in Moscow: %H:%M:%S')
        self.assertEqual(response.data.decode('utf-8'), msk_time)


if __name__ == '__main__':
    unittest.main()
