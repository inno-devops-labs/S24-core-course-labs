
# Python Web Application - Current Time in Moscow

### Framework Choice: Flask

I chose Flask for this web application for the following reasons:

1. **Lightweight:** Flask is a lightweight framework, making it easy to set up and get started quickly.

2. **Simplicity:** Flask follows a minimalistic design philosophy, making it simple and easy to understand. This is suitable for a small project like displaying the current time.

3. **Flexibility:** Flask provides just the basics for web development, allowing developers to choose and integrate components as needed. This flexibility is beneficial for this specific application.

4. **Active Community:** Flask has a large and active community, which means there are plenty of resources, tutorials, and support available.


## Coding Standards, Testing, and Code Quality

### Best Practices:

1. **Modular Design:** The application follows a modular structure for better organization and reusability.

2. **Configurability:** Critical settings, such as the MSK Time timezone, are externalized for easy adjustments.

3. **Consistent Naming Conventions:** The code adheres to consistent naming conventions for improved readability.

### Testing and Code Quality:

1. **PEP 8 Compliance:** The code strictly follows the PEP 8 style guide for Python.

2. **Unit Testing:** A comprehensive suite of unit tests ensures the functionality of individual code units.

3. **Integration Testing:** Integration tests cover interactions between different components, identifying potential issues.

4. **Continuous Integration (CI):** CI is implemented to run tests automatically upon each repository update.

5. **Code Reviews:** Two pull requests have been created, promoting collaboration and code quality.

6. **Linting:** Linting tools are employed to analyze and enforce coding standards.

## Testing and Code Quality

## Unit Testing

A suite of unit tests has been developed to ensure the correct functionality of the application. These tests validate key parts of the code, especially the display of the current Moscow time and date.

### Test Breakdown
- **test_current_time_displayed**: Verifies that the correct time is displayed on the main page and that the `index.html` template is used.
- **test_time_zone_offset**: Ensures that the displayed time has the correct Moscow offset of +3 hours.
- **test_content_contains_date**: Checks that the page content includes today’s date, formatted as `YYYY-MM-DD`.

### Running Unit Tests
To run the tests, navigate to the project root directory and execute:
```bash
python -m unittest test_app.py
```

## Testing Practices
Comprehensive Coverage: Tests are written to cover both basic functionality and edge cases.

Continuous Integration: CI pipelines automatically run these tests on each update, ensuring stable builds.

Test Documentation: Test instructions are documented here and in README.md to assist developers in understanding the testing structure and maintaining test coverage.