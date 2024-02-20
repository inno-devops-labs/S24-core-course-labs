# Python Web Application

## Justification for Using Flask Framework

To develop a simple Python web application for displaying
the current time in Moscow, I chose the Flask framework.

Flask is a lightweight and flexible web framework that
is well-suited for small to medium-sized projects. The decision
to use Flask for this specific application is based on several factors.

### Simplicity and Minimalism

Flask is known for its simplicity and minimalism.
It provides just what is needed for building web applications
without unnecessary complexity. Given the straightforward nature of
the task – displaying the current time in Moscow – Flask allows
for a concise and easy-to-understand implementation without
additional overhead.

```python
from flask import Flask
import time

app = Flask(__name__)

# ... (Implementation)
```

### Quick Setup and Deployment

Flask offers a quick and easy setup process.
With just a few lines of code, a basic web application can be created.
This simplicity is beneficial for rapid development and deployment,
making it an ideal choice for small projects or prototypes.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

### Routing and URL Handling

Flask's routing system is intuitive and allows for easy definition
of endpoints. In this application, the route '/' is defined to display
the current time in Moscow. This makes the code organized and readable.

```python
@app.route('/')
def display_moscow_time():
    moscow_time = get_moscow_time()
    return f"Current time in Moscow: {moscow_time}"
```

### Flexibility and Extensibility

While Flask is lightweight, it provides flexibility and can be extended
as needed. This flexibility makes it adaptable for a wide range of
projects, including small applications like the one being developed here.

### Conclusion

Considering the simplicity of the task, the need for quick development,
and the minimalistic nature of the application, Flask emerges as a
suitable choice. It allows for a clean and straightforward
implementation, making the development process efficient and the
codebase easy to maintain.

## Best Practises

I used `pytz` and `datetime` libraries because It's generally
recommended to use such modules for accurate
and reliable time zone handling

I used <https://www.pythonchecker.com/> with PEP8 style guide for Python
and got `72%` of code quality which considered as `Very Good`

## Unit Tests Description and Best Practices

### Test Cases

#### 1. `test_display_moscow_time`

- **Objective**: Ensure that the application displays the current time in Moscow correctly.
- **Steps**:
  1. Send a GET request to the root route of the application.
  2. Extract the response data and decode it.
  3. Get the current time in the Europe/Moscow timezone.
  4. Format the current time as expected for comparison.
  5. Compare the response data with the expected formatted time.
- **Assertions**:
  - Assert that the response status code is 200.
  - Assert that the response data matches the expected formatted time.

#### 2. `test_invalid_route`

- **Objective**: Ensure that the application returns a 404 status code for an invalid route.
- **Steps**:
  1. Send a GET request to an invalid route of the application.
  2. Check the response status code.
- **Assertions**:
  - Assert that the response status code is 404.

### Best Practices Applied

#### 1. Isolation with setUp Method

- **Description**: The `setUp` method is used to create a test client for the Flask application before each test case. This ensures that each test case operates on a clean and isolated environment.
- **Benefit**: Ensures reproducibility and independence of tests by providing a consistent setup for each test case.

#### 2. Descriptive Test Method Names

- **Description**: Test methods are named according to the behavior they test, such as `test_display_moscow_time` and `test_invalid_route`.
- **Benefit**: Provides clarity and documentation about the purpose of each test case, aiding in understanding and maintaining the test suite.

#### 3. Assertion Messages

- **Description**: Assertion messages are not explicitly provided in the test cases, but the use of descriptive method names and comments enhances readability and understanding.
- **Benefit**: Improves the clarity of test failures by providing context and explanation about the expected behavior.

#### 4. Separate Test Suite Execution

- **Description**: The test suite is executed using `unittest.main()` within the `if __name__ == '__main__':` block.
- **Benefit**: Allows the test suite to be executed independently of other code, facilitating integration with CI/CD pipelines and development workflows.

### Test Cases Conclusion

The unit tests follow best practices in terms of isolation, descriptive naming, clarity, and separate execution, ensuring robust validation of the Flask application's functionality.
