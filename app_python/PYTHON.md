## Reasons to choose FastAPI over other frameworks

- Performance: FastAPI is known for its high performance, making it suitable for real-time applications
- Automatic API Documentation: FastAPI automatically generates interactive API documentation (Swagger UI) based on your code, which is very helpful
- Built-in type annotations: FastAPI provides compatibility with Python type annotations for defining routes, request bodies, and responses, which improves code readability and correctness




## Best Practices and Coding Standards

In the development of the Python web application, several best practices and coding standards were adhered to, ensuring code quality and maintainability.

- Constants: Application utilizes constants for a better codebase readability and understandability 
- PEP 8 Compliance: The codebase followed the guidelines outlined in PEP 8
- Documentation: Docstring was included into main function, providing clear explanation of its purpose, parameter, and return value
- Type Annotations: Type hints were utilized, following Python 3.7+ type annotation conventions
- Testing: Code is covered by tests following best practices. This ensures correct behaviour of codebase

## Unit Tests

Comprehensive unit tests were created for the application to verify its functionality and behavior:

- **test_status**: This test checks if the HTTP status code of the response from the application's index URL is 200 (OK). It ensures that the application is accessible and responding correctly to requests.
- **test_text_changes**: This test verifies that the text content of the response from the application's index URL changes over time. It waits for 3 seconds between two requests and compares the text content of the responses to ensure that it has changed.
- **test_time_equality**: This test validates the correctness of the time displayed by the application. It extracts the time text from the response, parses it into a datetime object, and compares it with the current system time. This ensures that the time displayed by the application matches the current time.


### Best Practices

In addition to implementing unit tests, various best practices were applied:

- Isolation: Each test is independent and isolated from other tests to ensure that failures in one test do not impact the execution of others
- Test Coverage: Aim for high test coverage by testing all critical paths and edge cases in the application 
- Continuous Integration: Implement continuous integration practices to automate the execution of tests whenever changes are made to the codebase

