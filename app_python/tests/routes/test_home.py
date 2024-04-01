from unittest import TestCase

from app import app


class TestWelcome(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_date_display(self):
        res = self.app.get("/")
        assert res.status_code == 200
