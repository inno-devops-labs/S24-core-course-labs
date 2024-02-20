# PYTHON.md

## Web Application Details

### Framework Choice

I chose Flask as the web framework for this application. Flask is a lightweight framework, that suitable for small
projects. Flask is widely used in the Python community, which means ample documentation and community support.

### Best Practices and Coding Standards

I followed several best practices and coding standards to ensure the quality and maintainability of the web application:

- **Project Structure:** The code is organized into modular components, adhering to the principle of separation of
  concerns. The application logic is contained in `app.py`, HTML templates in the `templates` folder, and static files (
  CSS) in the `static` folder.

- **Timezone Handling:** The application uses datetime and pytz libraries for time calculations to ensure consistency.
  It converts the UTC time to the Moscow timezone for display.

- **HTML Template**: HTML templates are used to separate the structure of the web pages from the application logic. This
  approach makes it easier to manage and update the visual aspects of the application without modifying the underlying
  Python code.

- **CSS Styling**: Styling is applied using an external CSS file (style.css). This practice promotes the separation of
  concerns by keeping the presentation logic separate from the application logic. The styling is kept simple and focused
  on improving the visual presentation of the web page.

### Testing

The application has undergone testing to ensure its functionality and reliability:

- **Manual Testing:** The application has been manually tested to verify that the displayed time accurately reflects the
  current time in Moscow. Additionally, the time updates correctly upon refreshing the page.

- **Debug Mode:** The application is set to run in debug mode during development (`app.run(debug=True)`). This mode
  provides detailed error messages and facilitates the identification and resolution of issues.

- **Unit Tests with Pytest:** Unit tests have been implemented using Pytest to ensure the correctness of specific functions. These tests cover the display of time, the conversion of time zones, and the HTML template rendering.

  - **Isolation:** Each unit test is designed to be isolated and independent of other tests. This ensures that a failure in one test does not affect the execution of others.

  - **Fixture Usage:** The `pytest.fixture` decorator is used to create fixtures, such as the test client. This promotes code reusability and avoids code duplication.

  - **Assertions:** Meaningful assertions are used in tests to clearly specify the expected behavior. For example, asserting the HTTP status code, presence of specific text, or correct rendering of HTML templates.

### Code Quality

- **Readability:** The code is written using meaningful variable and function names.

- **PEP 8 Compliance:** The code adheres to the PEP 8 style guide for Python.

- **Version Control:** The project is version-controlled using a tool like Git. This allows for tracking changes and
  rolling back to previous versions if needed.
