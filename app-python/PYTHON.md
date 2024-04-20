## Choice of framework


I chose ``Flask`` for this project due to following reasons:
 - It is well-suited for small projects:)
 - It is easy to insert content into HTML templates using it.
 - It has build-in development server for testing.

## Best practices

- Logging: use ``logging`` library for printing logs into ``app.log`` file
- ``.gitignore``: use it to stash logs.
- Error handling: add ``error.html`` template to render it in case of errors.
- Testing: wrote test for validating if rendered time is correct using ``unittest`` library.
- ``requirements.txt`` with dependencies by <code>pip freeze > requirements.txt</code> command.
- Store all HTML templates into separate folder ``templates``
- Follow Python's PEP 8 style guide for code consistency.

## Code quality

- I used ``Pylint`` linter for code formatting.


### Unit tests

1. **test_moscow_time_calculation**: This test ensures that the displayed time on the homepage (`/`) is correctly calculated as the current UTC time plus 3 hours, which corresponds to Moscow time. It compares the expected Moscow time string with the actual displayed time string on the webpage.

2. **test_template_rendering**: This test checks that the homepage (`/`) renders the correct template, which includes the text "Current time in Moscow:".

3. **test_error_route**: This test checks that the error route (`/error`) returns a status code of 200 (OK) and includes the expected error message "An error occurred" in the response data.

#### Best practices for tests

1. **setUp Method:** The `setUp` method is used to set up the test client and configure it for testing. This ensures that these steps are executed before each test method, keeping the tests isolated and reducing duplication.

2. **Test Isolation:** Each test method is independent and does not rely on the state set by other tests. This ensures that the tests can be run in any order and are not affected by each other.

3. **Descriptive Test Names:** The test methods have descriptive names that clearly indicate what aspect of the application they are testing. This makes it easier to understand the purpose of each test.

4. **Use of Assertions:** Specific assertions (`self.assertEqual` and `self.assertIn`) are used to verify the expected behavior of the application. These assertions test exactly what is intended to be verified.

5. **Handling of Exceptions:** The `display_time` route includes exception handling, ensuring that both the normal behavior and any exceptional cases are covered by the tests.


