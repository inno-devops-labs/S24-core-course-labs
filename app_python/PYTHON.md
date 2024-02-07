# Python Web Application Description

## Framework choice:

The main framework chosen for this web application is Flask.

**Why Flask?**
   - Simplicity, flexibility, and suitability for small-scale web applications.
   - Lightweight and easy-to-use framework.
   - Minimal boilerplate code, allowing rapid development. 

## Best Practices Applied:

1. **Modularization**: The application is structured into separate files for better organization and maintainability.

3. **Timezone Handling**: The application uses the pytz library to handle timezones effectively, ensuring accurate time representation for the Moscow timezone.

4. **Template Rendering**: HTML content is separated from the Python code using Flask's `render_template` method, promoting code readability and maintainability.

5. **Docstrings**: Docstrings are included in functions to provide documentation and enhance code understanding.

## Testing
   - Unit tests are implemented to ensure functionality correctness.
   - The `test_app.py` file contains unit tests for the main endpoint of the application.
   - The tests verify that the endpoint returns a status code of 200 (OK) and contains the expected content.
   - Additionally, a time correctness test is included to verify that the displayed time is correct.