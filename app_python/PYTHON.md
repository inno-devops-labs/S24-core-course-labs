## Flask framework for my web application
### Reasons:
1. Quick Start:
   Setting up Flask is fast and easy. It's simple to learn, which means we can get our basic web app running quickly.
2. Great for Small Projects: 
Flask is ideal for small to medium projects like ours. It offers the right mix of simplicity and flexibility, letting us get our web app up and running without unnecessary complications.
3. Works Well with Python: 
As we're using Python for this project, Flask's way of working fits nicely with Python's principles. This means we can smoothly use Python tools in our Flask app.

## Best practices applied in the web application
### Coding standards
1. PEP 8 Compliance:
   - The Python code adheres to PEP 8 style guidelines, ensuring consistency in coding style, formatting, and best practices.
2. Descriptive Naming:
   - Meaningful and descriptive names are used for variables, functions, and classes.
### Testing
Manual testing was used to verify the functionality and interactions of the application.

## Unit tests
I have created unit tests for the Flask application using the unittest framework. The main test I wrote is test_display_time_msk, which tests the / route of the application to ensure it returns the current time in Moscow correctly.

### Best Practices Applied:
- Used the unittest.TestCase class to define test cases.
- Utilized the Flask test client to simulate requests and test responses.
- Checked response status codes and content to verify the correctness of the application output.
