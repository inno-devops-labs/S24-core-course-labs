# Simple Web Application

This application is a minimalistic web service that provides the current time in
Moscow.

## Prerequisites

Ensure you have [Python](https://www.python.org/) installed on your system. This
project uses [Poetry](https://python-poetry.org/) for dependency management.

## Installation

Clone the repository and navigate to the project directory. Install the
dependencies using Poetry:

```bash
poetry install
```

## Running the Application

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

## Testing

This project uses [pytest](https://docs.pytest.org/en/7.4.x/) for testing. It's
important to update and run tests to ensure the application's reliability. Run
the tests using the following command:

```bash
poetry run pytest
```

This version provides a bit more context and instructions, making it easier for
new users or contributors to understand and use your project.
