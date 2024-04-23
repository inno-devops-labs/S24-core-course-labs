# Python Web Application: Moscow Time Display

## Overview

This Python web application displays the current time in Moscow. It utilizes the Flask framework to create a lightweight web server at `http://127.0.0.1:5000/` and returns the current time in JSON format.

This app also have ```/visits``` endpoint, with the number of visits to the app.
The response is in JSON format:
```json
{"visits":14}
```

## Local Installation

Follow these steps to set up the application locally:

1. Clone this repository:

    ```bash
    git clone <repository_url>
    cd app_python
    ```

2. Install dependencies using pip and virtual environment:

    ```bash
        For linux:
        python -m venv venv && source venv/bin/activate
        For windows in GitBash:
        python -m venv venv && source venv/Scripts/activate
        pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Requirements

- Python 3.x
- Flask
- pytz
- freezegun
- prometheus_client

## Structure

- `app.py`: Contains the application logic.
- `requirements.txt`: Lists the dependencies required to run the application.
- `test_app.py`: Contains unit tests for the application.
- `PYTHON.md`: Describes best practices, coding standards, and testing approaches applied.
- `README.md`: Overview of the application.
- `.flake8`: Config for flake8 linter to run flake8 for whole project

## Docker

The application has been containerized using Docker. Follow the steps below to build, pull, and run the containerized application.

## Unit Tests

To run tests use `pytest` command (via venv).

### CI Workflow

The CI (Continuous Integration) workflow for this project automates the process of building, testing, and deploying the application. It ensures code quality, reliability, and security by following best practices in software development.

### Workflow Overview:

- **Automated Testing**: Unit tests are executed using `pytest` to verify the correctness of the codebase.
- **Code Linting**: `Flake8` is used to enforce coding standards and maintain consistent code style.
- **Security Scanning**: `Snyk` is integrated to check for vulnerabilities in dependencies and ensure application security.
- **Docker Integration**: `Docker` is utilized for containerization, enabling consistent deployment across environments.
- **Documentation**: Comprehensive documentation in `CI.md` outlines the best practices implemented in the CI workflow.

![CI Workflow Status](https://github.com/levpen/S24-core-course-labs/actions/workflows/python_workflow.yml/badge.svg)

### How to build?

To build the Docker image, run the following command:
```docker build -t my_app .```


### How to pull?

To pull the pre-built Docker image from the Docker Hub, run the following command:
```docker pull levgo/devopslab```


### How to run?

To run the containerized application, execute the following command:
```docker run -p 5000:5000 my_app```


After running the above command, you can access the application at http://localhost:5000.