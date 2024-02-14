import unittest
from flask import Flask, render_template
from app import app

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        expected_content = b'<h1>Current Time in Moscow:</h1>'
        self.assertIn(expected_content, response.data)

if __name__ == '__main__':
    unittest.main()
