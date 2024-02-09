# Time Table Web App

![example workflow](https://github.com/RamPrin/DevOps-S24/actions/workflows/pytest.yaml/badge.svg)

Simple web application written in go which shows the time in Moscow on each page reload.

## Prerequisites

Before launching application install `requirements.txt` using `pip`:

```bash
    pip install -r requirements.txt

```

## Starting the app

To start the server, run from `app_python` folder:

```bash
    go run server.go
```

Afterwards, this application will be available on `localhost:8080/`

## Docker

This application can be containerized with docker.

### Build or Pull

You can build a container by running:

```bash
docker build -t <TAG> app_python/
```

Or you can pull existing container from Docker Hub:

```bash
docker pull ramprin/devops:go
```

### Run

In order to run container use the following command:

```bash
docker run -p 80:8080 ramprin/devops:go
```

After this, your application will be available on <http://localhost>

## Unit Tests

The app contains some unit tests which can be started from `app_python` folder:

```bash
    pytest -rP .
```

Folder `test` contains 2 unit tests: 
- `test_root()`: check, whether root path returns a result
- `test_time()`: check if the time path retruns a valid time

## CI workflow

In `./github/workflows` folder you can find two workflows:

`ruff.yaml`- Linter workflow which checks if the code is properly formatted

`pytest.yaml`- This workflow has 3 stages:
    - Pytest: runs unit tests
    - Snyk: uses [snyk](https://snyk.io/) to check on vulnerabilities
    - Docker: builds the image and push it to the repository    



