# Project Name: Time Display Web Application

## Description

This web application displays the current time in Moscow. It is built with Flask, a lightweight WSGI web application framework in Python. The application demonstrates the use of Flask for creating web applications, handling routes, rendering templates, and displaying dynamic content based on the server's timezone.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Tests](#tests)
- [Best Practices](#best-practices)
- [License](#license)

## Installation

Follow these steps to set up your development environment:

1. **Clone the repository**


2. **Set up a virtual environment**

Navigate to the project directory.

Create a virtual environment:

```
python -m venv venv
```


Activate the virtual environment:

- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

3. **Install dependencies**

```
pip install -r requirements.txt
```


## Usage

To run the application locally:

1. **Start the Flask application**

```
python run.py
```


2. **Visit the application**

Open a web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Tests

To run tests, execute the following command:

```
python -m unittest discover -s tests
```

Ensure all tests pass before submitting a pull request for your changes.

## Best Practices

This project adheres to the following best practices:

- **Code Style**: Follows PEP 8 style guide for Python code.
- **Security**: Implements input validation and output encoding to protect against common vulnerabilities.
- **Testing**: Includes comprehensive unit tests to ensure functionality and prevent regressions.

For more details, refer to the [PYTHON.md](PYTHON.md) document.
