from django.test import TestCase, RequestFactory
import os
import sys
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)
from msk_time import views


class MyViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_my_view(self):
        request = self.factory.get('/msc_time/')
        response = views.MoscowTimeView.as_view()(request)
        self.assertEqual(response.status_code, 200)
