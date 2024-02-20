# Python Web Application - Current Time in Moscow

## Framework Choice:
I chose Flask as the framework for this Python web application because of its simplicity, flexibility, and suitability for small projects. Flask allows for quick development of web applications and provides the necessary tools to create a basic application like displaying the current time in Moscow.

## Coding Standards and Best Practices:
- Followed PEP 8 coding standards to ensure consistency in code formatting.
- Implemented proper separation of concerns by defining routes and logic in separate functions.
- Used the pytz library to handle timezones accurately and display the current time in Moscow.
- Utilized a virtual environment for dependency management to maintain project dependencies.
- Applied error handling to catch and handle exceptions that may occur during the application's execution.
- Documented the code with clear comments to enhance code readability and understanding.

## Testing:
- For testing the application, a test script `test_app.py` has been created using the `pytest` testing framework. This script includes a test function `test_get_time` that verifies the correctness of the response from the `get_time()` route. The test checks for the successful response status code, the presence of the message indicating the current time in Moscow, and validates the format of the displayed time to ensure accuracy in time representation.
- Also manual testing was applied: several runs of the app with checking the time after several refreshments comparing to the conventional time servers