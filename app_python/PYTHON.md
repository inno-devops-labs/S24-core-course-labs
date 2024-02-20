# Lab 1.
## Task 1;
Reasons for choosing the Flask framework:
- I have no experience working with python frameworks. I only know that there are 3 main ones: Django, Flask, and Pyramid. Of the above, it seemed to me that Flask is the most native and simple.
- Nevertheless, I already had a little experience working with Flask, where I prescribed endpoints for a server application.
Summarizing all the above, I chose Flask as the main framework for the application.

## Task 2;
## Best practices/coding standards used in this web application:
- It uses a ready-made framework for creating service endpoints and working with them, rather than self-written interactions with sockets directly.
- Using .gitignore file in order not to transfer unnecessary/confidential information to the repository
- Storing environment variables in .env .This will allow you to change them or dynamically change them in the future with CI/CD
- Using a docker container. There is a docker file in the directory that should be used to start the server.
- I wrote unit test for this simple python program (`test_app.py`)

# Lab 3
## Task 1;
### Describe the unit tests I've created:
1. TestApp Class:
- Inherits from unittest.TestCase: This is the standard way to create test cases in Python using the built-in unittest framework.
- Represents a test suite for testing the Flask application
2. setUp Method:
- Used for test setup: In this method, you configure the Flask application for testing.
- app.testing = True: This configures the Flask application in testing mode, which usually disables error catching during request handling.
- self.client = app.test_client(): This creates a test client for interacting with the Flask application in the test environment. This client allows you to send requests to the application and examine the responses.
3. test_get_time Method:
- Tests the functionality of the / endpoint in the Flask application.
- Sends a GET request to the / endpoint using the test client.
- Asserts that the response status code is 200, indicating a successful request.
- Asserts that the response data contains the expected string, indicating that the response includes information about the current time in Moscow.

### Best Practices Applied:
1. Isolation of Tests
Each test method is independent and doesn't rely on the state of other tests. This ensures that the tests can be run in any order without affecting the results.
2. Test Setup:
Using the setUp method to set up the test environment ensures that common configuration steps are performed before each test method is executed. This helps in keeping the test code DRY (Don't Repeat Yourself) and ensures consistency across tests.
3. Assertions:
Using self.assertEqual and self.assertIn for assertions ensures that the test results are clearly reported in case of failures. It also makes the test code more readable.
4. Main Guard:
- The if __name__ == '__main__': unittest.main() block ensures that the test suite can be executed directly by running the script, making it easy to run the tests without needing an external test runner.
