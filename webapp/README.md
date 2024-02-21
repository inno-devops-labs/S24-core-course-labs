# Moscow Time Django Web Application

## Overview

This Django web application provides an API endpoint that returns the current time in Moscow. It uses the `Django` framework along with the `pytz` library for handling time zones.

## Table of Contents

- [Features](#features)
- [Prerequisities](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example response](#example-response)
- [Docker](#docker)
- [Unit Tests](#unit-tests)
- [CI Workflow](#ci-workflow)

## Features

- Provides a RESTful API endpoint to retrieve the current Moscow time.
- Follows best practices for Django web application development.

## Getting Started

### Prerequisites

- Python 3.x
- `Django` framework
- `pytz` library

### Installation

1. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the Moscow time API endpoint:

    - URL: http://localhost:8000/moscow-time/
    - Method: GET
    - Response: JSON object containing the current Moscow time.

### Example Response

```json
{
  "moscow_time": "2024-02-05 12:34:56 MSK"
}
```

## Docker

### Building the Docker Image

To build the Docker image for this application, follow these steps:

1. Navigate to the root directory of the project.
2. Run the following command:
    ```bash
    docker build -t webapp .
    ```

### Pulling the Docker Image

If you prefer to pull the Docker image from a registry instead of building it locally, you can use the following command:

```bash
docker pull grisharybolovlev/webapp:v1.0
```

### Running the Docker container

To run the Docker container for this application, execute the following command:

```bash
docker run -p 8000:8000 webapp
```

This command will start the Django application inside a Docker container, and you can access it at http://127.0.0.1:8000 in your web browser.

## Unit Tests

Unit tests have been created to verify the functionality and behavior of various components within the Django application. These tests cover models, views, forms, and utility functions to ensure that individual units of code work as expected.

To run the unit tests, use the following command:

```bash
python manage.py test
```

This will discover and run all tests within the tests package of your Django app.

## CI Workflow
[![CI](https://github.com/GrishaRybolovel/S24-core-course-labs/actions/workflows/main.yml/badge.svg)](https://github.com/GrishaRybolovel/S24-core-course-labs/actions/workflows/main.yml)

A CI workflow has been set up using GitHub Actions to automate the build, test, and deployment process of the Django application. The workflow consists of the following essential steps:

1. **Install Dependencies**: Install project dependencies and set up the Python environment.

2. **Run Code Linting**: Check the code for style and potential errors using Flake8.

3. **Run Tests**: Execute the test suite of the Django application to ensure code correctness.

4. **Build and Push Docker Image**: If the tests pass successfully, build the Docker image for the Django application and push it to Docker Hub.

The CI workflow runs automatically on every push to the main branch and on pull requests targeting the main branch. It helps ensure that changes to the codebase do not introduce regressions and maintain code quality standards.
