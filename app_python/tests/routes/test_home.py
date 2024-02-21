from unittest import TestCase

from app import create_app


class TestWelcome(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_date_display(self):
        res = self.app.get("/")
        assert res.status_code == 200
