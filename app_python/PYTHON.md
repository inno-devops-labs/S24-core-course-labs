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

# Unit Tests

Unit tests have been implemented for the Flask web application to ensure its functionality remains consistent.

### Test Cases
1. **test_index**: Verifies that the root URL endpoint returns a status code of 200 (OK) and contains the expected string "The current time in Moscow:".
2. **test_time_correctness**: Verifies that the displayed time matches the current time in Moscow.

### Best Practices Applied
- Use of `unittest.TestCase` for organizing test cases.
- Use of `setUp()` method to set up the testing environment.
- Use of assertions such as `assertEqual()` and `assertIn()` to verify expected behavior.
- Use of BeautifulSoup for parsing HTML responses in tests to ensure accurate comparisons.