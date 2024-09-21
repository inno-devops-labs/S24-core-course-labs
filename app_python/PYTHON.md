# PYTHON.md

## Web Framework Choice: Flask

I chose Flask as the web framework for its simplicity, flexibility, and ease of use. Flask is well-suited for small applications.

## Web Application Description

- **Best Practices:**

  - Utilized Flask's modular structure.
  - Followed PEP 8 coding standards for clean and readable code.
  - Used a virtual environment for dependency isolation.

- **Testing:**

  - I used manual testing

- **Code Quality:**
  - Performed code reviews through two pull requests (PRs) for collaborative improvement.

### Unit Test: Testing Current Time Format

#### Purpose:

- The `test_current_time_format` unit test ensures that the Flask application endpoint `/` returns the current time in Moscow with the expected format `YYYY-MM-DD HH:MM:SS`.

#### Fixture Setup:

- The `client` fixture is set up using `pytest.fixture`, providing a test client to interact with the Flask application.

```python
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
```

#### Test Function:

- The `test_current_time_format` function sends a GET request to the `/` endpoint and verifies that the response contains the current time in the specified format.

```python
def test_current_time_format(client):
    response = client.get("/")
    data = response.get_data(as_text=True)
    assert response.status_code == 200
    assert re.match(
        r"The current time in Moscow is: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
        data,
    )
```

#### Best Practices Applied:

- **Fixture Usage**: Utilizes a fixture (`client`) to set up the test client, ensuring consistency and reusability in test setup.
- **Assertion**: Asserts the expected behavior of the Flask application, validating both the HTTP status code and the format of the response data.
- **Regular Expressions**: Employs a regular expression to verify that the response contains the current time in the expected format, enabling precise validation.
- **Modularity**: Separates fixture setup and test function, promoting clarity and maintainability of the test code.
