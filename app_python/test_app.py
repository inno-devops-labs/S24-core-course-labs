import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        response = self.app.get('/')
        self.assertIn(b'<div id="title">Moscow Time</div>', response.data)
        self.assertIn(b'<div id="clock"></div>', response.data)
        
    def test_title_content(self):
        response = self.app.get('/')
        self.assertIn(b'<title>Moscow Time Digital Clock</title>', response.data)

    def test_clock_script(self):
        response = self.app.get('/')
        self.assertIn(b'<script>', response.data)
        self.assertIn(b'function updateClock()', response.data)

if __name__ == '__main__':
    unittest.main()
