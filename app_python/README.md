# Python Web Application

This Python web application displays the current time in Moscow. Built with FastAPI, it demonstrates efficient handling of asynchronous requests and serves as an example of modern web application development in Python.

## Features

- Displays the current time in Moscow, updating dynamically with each page refresh.
- Built with FastAPI for high performance and ease of development.
- Utilizes HTML and CSS for a simple and responsive user interface.

## Getting Started

### Prerequisites

What things you need to install the software and how to install them:

```

python3 -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```

### Installing

A step by step series of examples that tell you how to get a development env running:

1. Navigate to the `app_python` folder:

```bash
cd app_python
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

The application will be available at `http://127.0.0.1:5000/` by default change `PORT` environment variable to change the port.


### Unit Tests

The application includes a suite of unit tests to ensure the functionality behaves as expected. Here's a brief overview of the tests:

- **Test for Time Updates**: This test checks that the time displayed updates correctly at least every 5 seconds, ensuring dynamic content is properly rendered.
- **Test for Time Format**: This test verifies that the time displayed matches the expected format (HH:MM:SS), ensuring data is accurately presented.

To execute the unit tests, ensure you have pytest installed and run the following command in the app root:

```bash
pytest
```

These tests are vital for maintaining the application's reliability and ensuring any new changes do not break existing functionality.

## Docker Usage

This section covers building, pulling, and running the Docker container for the application.

### Building the Docker Image

To build the Docker image, run the following command in the project app_python folder:

```bash
docker build -t xdrdvd/app_python:latest .
```

### Pushing the Docker Image

To push the Docker image to Docker Hub, run the following command in the project app_python folder:

```bash
docker push xdrdvd/app_python:latest
```

### Pulling and running the Docker Container

To pull and run the Docker container, run the following commands:

```bash
docker pull xdrdvd/app_python:latest
docker run -p 5000:5000 xdrdvd/app_python:latest
```

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Python](https://www.python.org/) - Programming Language
- [docker](https://www.docker.com/) - Containerization

## CI/CD
![python app workflow](https://github.com/ahmedXDR/S24-core-course-labs/actions/workflows/python-ci.yml/badge.svg)
