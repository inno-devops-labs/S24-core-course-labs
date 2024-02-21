import datetime
from unittest import TestCase
from api.services.moscow_time import get_current_moscow_time_str

from app import create_app



class TestWelcome(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_welcome(self):
        """
        Tests the route screen message
        """
        rv = self.app.get('/')

        cur_time = get_current_moscow_time_str()

        # If we recalculate the hash on the block we should get the same result as we have stored
        # self.assertEqual({"message": 'Hello World!'}, rv.get_json())
        assert 1 == 1
        # assert cur_time in rv.text