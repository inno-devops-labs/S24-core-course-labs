# Python Web Application Details

## Chosen Framework: Flask

I have chosen Flask because it is quite simple, so it is suitable for this small web application.

## Best Practices Applied:

- Used a virtual environment for dependency management.
- Followed PEP 8 coding standards.
- Ensured code quality by applying modular design principles.
- Tested my app manually (on local machine)

## Code Quality:

The code has been linted using Flake8 to ensure adherence to PEP 8 standards.

## Unit Tests

### Description

We have implemented unit tests using the `pytest` framework to ensure the functionality and reliability of our Flask
application. The primary test, `test_display_time`, is designed to verify that the home route returns the expected
content.

### Test Details

#### `test_display_time`

This test utilizes a Flask test client to simulate a request to the home route (`'/'`). It checks if the response
contains the expected content, confirming that the time display functionality is working correctly.

### Best Practices Applied

1. **Fixture Usage:** We utilized the `pytest.fixture` decorator to set up a test client with the application configured
   for testing. This ensures a clean testing environment.

2. **Clear Test Naming:** Test names are descriptive and follow the convention of starting with "test_". This promotes
   clarity and readability in the test suite.

3. **Isolation:** Each test is designed to be independent, testing a specific aspect of the application's functionality.
   This promotes maintainability and ease of debugging.

4. **Framework Choice:** We opted for the `pytest` testing framework due to its simplicity, powerful features, and
   widespread adoption in the Python community.
