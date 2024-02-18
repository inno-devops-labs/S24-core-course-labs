# Justification for Using Flask

Flask is a lightweight and easy-to-use web framework for Python. The choice of Flask for this web application is justified due to its simplicity, flexibility, and ease of use for small projects. It allows us to quickly set up a web server and handle the display of the current time in Moscow with minimal boilerplate code.

## Best Practices and Coding Standards

- Project Structure: The application follows a standard Flask project structure with a separate templates folder for HTML templates.
- Code Modularity: The application is modular with a clear separation of concerns. The logic for retrieving and formatting the Moscow time is in the `main.py` file, while the HTML template is in the templates folder.
- Datetime and Timezone Handling: The datetime and pytz libraries are used to handle time and timezones appropriately. This ensures accurate and reliable time information.
- HTML Templating: The use of Flask's HTML templating engine allows for dynamic content rendering and a clean separation of backend logic and frontend presentation.

## Testing and Code Quality

- Debug Mode: The application is set to run in debug mode using `app.run(debug=True)` during development for easier debugging.
- Manual Testing: The application has been tested manually to ensure that the displayed time updates upon page refreshing.
- Code Review: Code has been reviewed to ensure adherence to PEP 8 coding standards, including proper indentation, clear variable naming, and code readability.

## Unit Tests

- We have included comprehensive unit tests for our Python Flask web application. These tests verify the functionality of different parts of the application, including getting the time, the time formatting and the general workflow itself.
- We have applied best practices by ensuring each test case is isolated and tests a specific functionality of the application.
- These tests use the standard unittest library for testing.