# Simple Web Application

![GitHub Actions Workflow][workflow-badge]

[workflow-badge]: https://github.com/fedor-ivn/devops/actions/workflows/python.yml/badge.svg

This application is a minimalistic web service that provides the current time in
Moscow.

## Prerequisites

Ensure you have [Python](https://www.python.org/) installed on your system. This
project uses [Poetry](https://python-poetry.org/) for dependency management.

## Running in Docker

To run the application in a Docker container, use the following commands:

```bash
docker pull fedorivn/simple-web-app:python-1.0.0
docker run --name app -d -p 8000:80 fedorivn/simple-web-app:python-1.0.0
```

## Installation

Clone the repository and navigate to the project directory. Install the
dependencies using Poetry:

```bash
poetry install
```

## Running Locally

Start the application using the following command:

```bash
poetry run python main.py
```

Upon successful startup, you should see output similar to this:

```bash
INFO:     Started server process [29565]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

You can now access the service by visiting `http://127.0.0.1:8000`. For example:

```bash
$ curl http://127.0.0.1:8000
{"current_time":"2024-01-31 14:16:05"}
```

The service also counts the number of visits to the main page. To obtain the
number of visits. The information is persistent because it is stored in a file
(`data/visits.txt`) that is created during the first run of the application. To
view the current number of visits, access the `/visits` endpoint:

```bash
$ curl http://127.0.0.1:8001/visits
{"visits":1}
```

## Building the Docker Image

To build the Docker image, use the following command:

```bash
docker build -t simple-web-app:python .
```

## Unit Testing

This project uses [pytest](https://docs.pytest.org/en/7.4.x/) for testing. It's
important to update and run tests to ensure the application's reliability. Run
the tests using the following command:

```bash
poetry run pytest
```

## Continuous Integration (CI)

The project uses a robust Continuous Integration:

1. Linting with Ruff
2. Build & Testing
3. Security checks with Snyk
4. Push to Docker Hub

The CI process is automated using GitHub Actions and leverages the best
practices described in [Best Practices][ci].

[ci]: ./CI.md
