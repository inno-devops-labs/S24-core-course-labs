# PYTHON.md

This document outlines the rationale behind the choices made during the development of Python web application that displays the current time in Moscow.

## Framework Selection
Flask framework chosen for its simplicity and ease of use. It allows us to quickly set up routes and render templates, which is perfect for our minimalistic application. Flask's lightweight nature makes it ideal for small projects and reduces the complexity of our setup.

## Best Practices
* DRY(Don't Repeat Yourself) principles applied by using modular code and separating concerns, such as rendering and business logic.
* Readability prioritized by using clear and descriptive variable and function names.
* Code maintainability ensured by organizing our project structure logically and keeping our functions focused and small.
* The PEP 8 coding standards style guide followed for Python code, including naming conventions, whitespace usage, and other formatting guidelines.
* CSS utilized to style HTML elements, keeping the code organized and maintainable.

## Testing
* While our application is simple, python web application manually tested by browser Chrome.

# Unit Tests

We've used `pytest` to write unit tests for our Flask application. The tests ensure that the `index` route returns a  200 status code and includes the expected text.

Best practices applied in testing include:

- Using fixtures for setup and teardown.
- Writing tests to be independent and repeatable.
- Using `assert` statements to validate the expected outcomes.
