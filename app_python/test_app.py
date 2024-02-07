import unittest
from app import app
from datetime import datetime
import pytz

class TestApp(unittest.TestCase):
       
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
       
    
    # Verify that the endpoint returns a status code of 200 (OK)
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The current time in Moscow:", response.data)
        
    # Verify if the displayed time matches the current time in Moscow
    def test_time_correctness(self):
        response = self.app.get('/')
        moscow = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S').encode('utf-8')
        self.assertIn(current_time, response.data)

if __name__ == "__main__":
    unittest.main()
