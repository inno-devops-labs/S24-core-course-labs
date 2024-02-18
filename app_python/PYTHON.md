# Python Web Application Framework Choice

## Flask

Flask has been chosen for this project due to its simplicity and lightweight nature. It provides the necessary tools and features to develop a web application quickly. Therefore, Flask is a suitable framework for a simple application that displays the current time in Moscow.


To update the `PYTHON.md` file with the best practices applied in your web application, you should elaborate on the following areas: coding standards adherence, testing strategy, and measures taken to ensure code quality. Below is a template you can use to update your `PYTHON.md` file, which reflects these considerations.

---

# Best Practices applied in the Web Application Development

## Coding Standards

### PEP 8 Compliance
The application adheres to [PEP 8](https://pep8.org/). The code is PEP 8 compliant by:

- Following naming conventions for variables, functions, classes, and modules.
- Keeping line lengths under 79 characters for code and 72 for comments to enhance readability.
- Using whitespace effectively to separate logical sections of code.

### Pylint Integration
`app.py` has a 10/10 score. It ensures that the code remains clean, well-documented, and easy to navigate, which leads to a more robust and reliable application.



## Testing

### Unit Testing
Unit tests were written to ensure that the application works correctly. The Python's `pytest` framework was used for this purpose.

#### Test Cases
1. **Test Show Time Status Code**: verifies that the / endpoint responds with a 200 HTTP status code, indicating a successful request.
2. **Test Show Time Content**: ensures that the / endpoint renders the correct template with the expected context variables.
3. **Test Home Page Moscow Time Display**: checks that the home page correctly displays the current Moscow time.
#### Best Practices applied in Testing
1. Test Isolation
- Each test is written to be independent of others, ensuring no shared state or side effects between tests.
2. Continuous Integration (CI)
- Integrating these tests into a CI pipeline ensures that tests are automatically run for every change, helping to catch issues early.
3. Naming Conventions and Documentation
- Standard naming conventions for test files and functions is used to ensure clarity and discoverability. Each test is documented to describe its purpose and methodology.
4. Use of Fixtures
- Fixtures are used for setting up the test environment and providing a reusable set of tools for multiple test functions. 
5. Context Manager for Resource Management
- Context Manager is utilized to manage resources efficiently, ensuring proper setup and teardown actions. It is particularly useful for testing that the correct templates are rendered with the expected context variables.

## Code Quality

### Structured Project Layout
The project has a clear structure, separating concerns and making the codebase easy to navigate. This includes:

- Keeping the application logic within `app.py`, tests logic within `test_app.py`.
- Storing HTML templates in a templates directory.

### Test Coverage
Test coverage stands at 93%. This high level of coverage means that the vast majority of the code is exercised by tests.