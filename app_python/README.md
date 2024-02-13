# Python Web Application

This is a simple Python web application that displays the current time in Moscow.

## Overview

The application is built using the FastAPI framework, providing high performance and automatic API documentation generation.

When starting the app, it's starts the web server on ```127.0.0.1:8080``` by default. The test file with env variables is provided in ```env.test```

Then the app accept GET requests on ```/```, which returns the OK status code with json in format
```json
{"time":  "2024-02-05 00:02:29"}
```

## Installation

1. Clone this repository.
2. Navigate to the `app_python` folder.
3. Ensure to have at least `Python 3.9.6`
4. Create a virtual environment ```python -m venv venv && source venv/bin/activate```
5. Install dependencies using `pip install -r requirements.txt`.

## Usage

1. Run the application using `python main.py`.
2. Access the application at `http://localhost:8000`.

## Testing

1. Run tests using `pytest` (using the venv).

## Structure

- `main.py`: Contains the main application logic.
- `test_main.py`: Contains unit tests for the application.
- `requirements.txt`: Lists the dependencies required to run the application.
- `PYTHON.md`: Describes best practices, coding standards, and testing approaches applied.
- `README.md`: Is current file, which is overview of the app.
- `env.test`: Example of env variables
- `.flake8`: Config for flake8 linter

## Docker

Docker must be installed and daemon is running.

### build (yourself) and run:
```
docker build -t devops-lab-02 .
docker run -p 8080:8080 --rm -ti devops-lab-02
```

### or

### pull the image and run it:
```
docker pull bulatok4/devops-lab-02 
docker run -p 8080:8080 --rm -ti bulatok4/devops-lab-02
```


