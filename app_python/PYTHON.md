# Justification for Flask

## Why Flask?

Flask was chosen for this project because of its simplicity. Since the application's requirements are quite easy, Flask provides the features without any complexity. And since the purpose of the course is DevOps engineering practice, not the Web Development, I think Flask would be quite optimal and straightforward framework.

## Best practices

- In my project, i will use git as source code management. So i prepared a proper `.gitignore` file for python projects.

- Used proper file naming, as well as proper class, variables naming.

- Described starting points in `README.md`. All the steps and requirements.

- Used unit tests for testing the business logic behind the `app.py`

# Unit Test Best Practices and Tests

## Applied Best Practices:

1. **Separation of Concerns**: Tests are separated into distinct methods, each testing a specific aspect of the application.

2. **Setup Method**: Utilization of `setUp()` method to initialize the test client and set testing to True.

3. **Assertion Usage**: Using assertions to verify the expected behavior in the tests.

4. **Isolation**: Ensuring tests do not interfere with each other by using separate requests for each test.

5. **Main Guard**: Including a main guard to ensure the tests are only run when the script is executed directly.

## Unit Tests:

```python
import time
import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_check_status(self):
        response = self.app.get('/')
        assert response.status_code == 200

    def test_get_moscow_time(self):
        response1 = self.app.get('/')
        time.sleep(1)
        response2 = self.app.get('/')
        
        self.assertNotEqual(response1.data, response2.data)

if __name__ == '__main__':
    unittest.main()

