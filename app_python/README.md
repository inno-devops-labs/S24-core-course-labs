# Moscow Time WebApp

## Overview

This is a very simple Python web application built with Flask to display the current time in Moscow.

## Getting Started

### Prerequisites

- Python
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Orillio/S24-core-course-labs.git
   ```

2. Navigate to the project directory:

   ```bash 
   cd S24-core-course-labs/app_python
   ```
2. Install the required dependencies
   ```bash 
   pip install -r requirements.txt
   ```

Usage

## Run the Flask application:

```bash
python app.py
```
Open your web browser and visit http://127.0.0.1:5000/ to view the current time in Moscow.

## Building and running docker

To run the application as docker container:

```bash
docker pull orillion1/lab2
```

```bash
docker run -p 5000:5000 lab2
```

The application will be accessible at `127.0.0.1:5000`

## Unit Tests

Run the provided unit tests to ensure the application is working correctly:

```bash
python -m unittest test_app.py
```
These are the unit tests that are currently implemented:

- `test_get_moscow_time`: Asserts the difference between time data of two responses.
- `test_check_status`: Checks the availability of page. Asserts 200 status

## CI/CD

CI/CD is designed for automatization of routine tasks, such as linting, building and pushing, which can be done automatically. These are the steps of implemented CI.

1. Checkouts main directory
2. Configures Python with 3.12 version
3. Installs pip and upgrades it
4. Installs needed requirements inside requirements.txt
5. Installs flake8
5. Runs flake8 against MCC and linter warnings
5. Run tests
6. Snyk analysis of vulnerabilitites
7. Docker Hub login
8. Docker image building
8. Docker image pushing

## Dependencies

* Docker
* Flask
* pytz