# Python Web Application

## Framework Choice: Flask

I chose to use the Flask framework for this Python web application for the following reasons:

- **Simplicity**: Flask is a lightweight and easy-to-use framework, which makes it ideal for small projects and prototyping.
- **Flexibility**: Flask allows for flexibility in project structure and doesn't impose strict conventions, making it easy to customize according to project requirements.
- **Suitability**: For a simple web application like displaying the current time in Moscow, Flask provides all the necessary features without unnecessary complexity.

## Additional Notes

- The application displays the current time in Moscow by utilizing the `pytz` library to handle time zones.
- The code follows best practices and coding standards recommended for Flask applications.

## Best Practices Applied

1. **Modular Structure**: The application follows a modular structure with separate modules for routes, templates, and static files, promoting code organization and maintainability.

2. **Flask Framework**: Leveraging Flask, a lightweight and modular micro web framework, allows for easy development and scalability of the application.

3. **Template Rendering**: HTML templates are used for rendering views, separating presentation logic from business logic.

## Coding Standards

1. **PEP 8**: Coding style adheres to the PEP 8 guidelines, ensuring consistency and readability throughout the codebase.

2. **Descriptive Naming**: Descriptive and meaningful variable and function names are used, enhancing code readability and maintainability.

## Testing

**Manual testing** since the problem is quite simple(all business logic is literally just 3 lines of code), so I conclude that manual testing is enough

# Unit Testing in Python

## Overview

Unit testing is an essential practice in software development that involves testing individual components or units of code to ensure their correctness and functionality. In this document, we describe the unit tests created for the Flask web application and discuss the best practices applied during their implementation.

## Unit Tests

### 1. `test_display_time`

This test case validates the functionality of the `display_time` route in the Flask application. It ensures that the response status code is 200 (indicating success) and that the response data contains the expected string indicating the current time in Moscow.

### 2. `test_time_between_requests`

In this test case, we measure the time taken to make a request to the `'/'` route and assert that it is less than 1 second. This test ensures that the response time of the application remains within an acceptable range.

### 3. `test_time_difference_between_requests`

This test case verifies the time difference between two consecutive requests to the Flask application. It makes the first request, sleeps for 1 second, and then makes the second request, ensuring that the time difference between the two requests is approximately 1 second.

## Best Practices

- **Descriptive Test Method Names:** Each test method is named descriptively to clearly indicate the purpose of the test.
- **Test Coverage:** The unit tests cover critical parts of the Flask application, including individual routes and functionality.
- **Testing Independence:** Each test case is independent and does not rely on the state of previous tests, ensuring consistent and reliable test results.
- **Precision in Timing:** Where applicable, precise timing measurements are used to validate response times and time differences between requests.