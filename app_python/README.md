# Flask Web Application
[![app python](https://github.com/itoqsky/S24-core-course-labs/actions/workflows/main.yml/badge.svg?branch=lab3)](https://github.com/itoqsky/S24-core-course-labs/actions/workflows/main.yml)

This simple Flask web application displays the current time in Moscow. It serves as a demonstration of best practices in web development.

## Installation:

1. Clone the repository:

   ```bash
    git clone <repository_url>
    cd app_python
    pip install -r requirements.txt
    python3 app.py
    python3 -m unittest test_app.py

## Docker

1. Building the Docker Image
   
   ```bash
   docker build -t python-app .

2. Pulling the Docker Image
   ```bash
   docker pull itoqsky/python-app


3. Running the Docker Image
   ```bash
   docker run -p 5555:5555 python-app


## Unit Tests

In this project, we use Python's built-in `unittest` module to write and run our unit tests.

To run the unit tests locally, use the following command:

`python3 app_python/test_app.py`

## Continuous Integration

Our project utilizes GitHub Actions to establish an automated integration process. This setup ensures that our Python application is automatically built and tested each time changes are committed to the main branch or when a pull request is initiated.

The integration process is comprised of the following sequence of actions:

- Code retrieval
- Configuration of Python 3.8 environment
- Dependency resolution
- Code analysis using flake8
- Execution of unit tests with pytest
- Docker image creation and deployment

To monitor the progress of the integration process, navigate to the "Actions" tab at the top of the repository.