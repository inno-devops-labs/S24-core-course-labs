# Python Web Application Development

## Framework Choice

For this project, Flask was chosen as the web framework due to its simplicity, flexibility, and lightweight nature. Flask is well-suited for small to medium-sized web applications and provides enough freedom to structure the project as needed without imposing too much boilerplate code. This makes it perfect for a straightforward application like displaying the current time in Moscow.

## Best Practices Applied

Several best practices have been applied in the development of this web application to ensure code quality, maintainability, and performance:

- **Code Organization**: The project structure is kept simple yet effective, with a clear separation between the application logic (`app.py`) and the documentation (`PYTHON.md` and `README.md`).
- **PEP 8 Compliance**: The code follows PEP 8 style guidelines, ensuring readability and consistency throughout the application.
- **Timezone Management**: The `pytz` library is used for accurate timezone conversions, ensuring the displayed time is always correct for Moscow.


### Unit tests

- Unit tests are implemented in the `tests/test_app.py` file:
  - Correct format of the displayed time.
  - Correctness of the route.
  - Correctness of the time value obtained from the system and the application.

## Testing

To run the tests, execute the following command:

```bash
python -m unittest tests.test_app.py
```
