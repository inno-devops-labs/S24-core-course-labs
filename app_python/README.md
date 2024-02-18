# Python Web Application - Moscow Time

![CI](https://github.com/hermandyudin/S24-core-course-labs/workflows/CI/badge.svg)

## Overview

This is a simple web application developed in Python using the Flask framework to display the current time in Moscow.

## Installation

1. Clone the repository:

```
git clone https://github.com/hermandyudin/S24-core-course-labs.git
cd app_python
```

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Running the Application

```
python app.py
```

Visit http://127.0.0.1:5000/ in your browser to view the work of the application.

## Docker

### Build

To get and run the Docker image, use the following commands:

```bash
docker pull dudukk/devops:latest
docker run -p 5000:5000 dudukk/devops:latest .
```

## Unit Tests

We have implemented a suite of unit tests to ensure the correctness of our Flask application. These tests cover
different aspects of the application's functionality, providing a robust foundation for development and maintenance.

### Running the Tests

To run the unit tests locally, follow these steps:

1. Go to the project root

2. Install the project dependencies:
   ```bash
   pip install -r app_python/requirements.txt
3. Run the tests using pytest:
   ```bash
   pytest

## Continuous Integration (CI) Workflow

Our project uses GitHub Actions for continuous integration. The CI workflow includes the following steps:

1. **Dependencies:** Install project dependencies.
2. **Linter:** Run pylint to check code quality.
3. **Tests:** Execute unit tests using `pytest`.
4. **Docker:** Build and push a Docker image to Docker Hub.

### Running CI Locally

To replicate the CI workflow locally, you need to have the necessary dependencies installed, including Docker.
Additionally, set up Docker Hub credentials as secrets in your GitHub repository.

```bash
pip install -r app_python/requirements.txt
pytest
```