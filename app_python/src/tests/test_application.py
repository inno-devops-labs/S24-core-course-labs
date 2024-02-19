import timeit
import unittest

import time
from app_python.src.moscow_time.app import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_display_time(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The current time in Moscow is:', response.data)

    def test_time_between_requests(self):
        # Measure time for making 10 requests
        time_taken = timeit.timeit(lambda: self.app.get('/'), number=10)

        # Calculate average time per request
        avg_time_per_request = time_taken / 10

        # Assert that average time per request is less than 0.1 seconds
        self.assertLess(avg_time_per_request, 0.1,
                        "Avg time per request should be less than 0.1 seconds")

    def test_time_difference_between_requests(self):
        # Make first request
        start_time = time.time()
        self.app.get('/')
        # Sleep for 1 second
        time.sleep(1)

        # Make second request
        self.app.get('/')
        end_time = time.time()

        # Calculate time difference between requests
        time_difference = end_time - start_time

        # Assert that time difference is approximately 1 second
        self.assertAlmostEqual(time_difference, 1.0, delta=0.01,
                               msg="Time dif between req must be about 1 s")


if __name__ == '__main__':
    unittest.main()
