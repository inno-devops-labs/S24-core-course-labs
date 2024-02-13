import time
import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_moscow_time(self):
        
        response1 = self.app.get('/')
        assert response1.status_code == 200
        time.sleep(1)
        response2 = self.app.get('/')
        assert response2.status_code == 200
        
        self.assertNotEqual(response1.data, response2.data)

if __name__ == '__main__':
    unittest.main()
