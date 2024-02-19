# Lab 1: Python Web Application

I made a decision to make Flask the main Framework for my app, because of its simplicity, perfomance and popularity

## Practises used

### Testing

Here are some generic best practices for writing unit tests in Python using the unittest framework:

1. Name test methods descriptively to indicate what aspect of the function is being tested.
2. Use assertEqual to check if the actual result matches the expected result.
3. Ensure each test method is independent and does not rely on the state of other tests.
4. Write tests that cover both positive and negative scenarios, including edge cases.
5. Use setUp and tearDown methods to set up and clean up resources needed for multiple test methods.
6. Keep test methods small and focused on testing a specific behavior or functionality.
7. Use meaningful assertions to clearly communicate the expected behavior of the code being tested.
8. Run tests frequently during development to catch bugs early and ensure code changes do not break existing functionality.
9. Maintain a good balance between unit tests, integration tests, and end-to-end tests to achieve comprehensive test coverage.

Following these best practices will help you write effective, maintainable, and reliable unit tests for your Python codebase.

### Separation of Concerns
Flask itself implements an MVC Pattern which separates code and template.

### Coding Standards
I used PEP 8 guidelines for Python code. This makes development of the app easier and enhances code readability. I also used modern development practises for HTML layout. 