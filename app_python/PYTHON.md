# Framework & Best Practices

## Justification for FastAPI Framework

I have chosen the FastAPI framework for the following reasons:

- FastAPI is known for its high performance and speed

- It provides a simple and intuitive coding experience, allowing developers to
  quickly develop APIs.

- FastAPI is widely adopted in the industry, which ensures good community
  support and a large ecosystem of libraries and tools.

## Best Practices

To ensure code quality and maintainability, I have applied the following best
practices to my web application:

- Used the `ruff` code formatter to enforce consistent code style and
  formatting according to various PEP-standards.

- Installed `pre-commit` hooks to automatically run code formatting, linting,
  and other checks before each commit.

- Installed `cspell` and created a dictionary to enable spell checking in code
  comments and documentation.

- Utilized the `poetry` package manager for dependency management, which
  provides a more robust, deterministic, and easy-to-use environment for
  managing project dependencies and environments.

- Leveraged the use of `devcontainers` in Visual Studio Code to create a
  consistent development environment, which can be shared and used by all
  developers, thereby eliminating the "it works on my machine" problem.

- Utilized `.gitignore` to keep the repository clean.

- Incorporated `.editorconfig` to define and maintain consistent coding styles
  between different editors.

- Added docstrings to document the purpose and usage of functions, classes, and
  modules.

- Utilized the `pytest` testing framework to write unit tests for the
  application.

These practices help in maintaining clean and readable code, improving code
quickly develop APIs.

## Unit Testing

For testing, I have used the `pytest` framework and the `TestClient` class from
`fastapi.testclient` to create a test client for easy testing of HTTP requests
and responses.

The primary responsibilities of my service, beyond the framework's
functionality, are:

1. Handling `GET HTTP` requests for the path `/` and ensuring that requests are
   accepted and responses are sent in the correct format.

2. Computing the current time in Moscow.

To ensure these functionalities are working as expected, I have conducted the
following tests:

1. **Time Equality Test (test_time_is_equal)**: The test asserts that the status
   code of the response is `200` and the time returned by the API is the same as
   the current Moscow time

2. **Time Change Test (test_time_have_changed)**: This test validates that the
   API correctly updates the time with each new request.
