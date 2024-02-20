![](https://github.com/ilnarkhasanov/S24-core-course-labs/actions/workflows/python-app.yml/badge.svg)

## Prerequisite

Install Python 3.12
Install Poetry - `$ curl -sSL https://install.python-poetry.org | python3 -`

## GitHub Actions
This repository contains a workflow for a checking an app on security (Snyk), testing (unit and integration), linting and pushing to the Docker Hub.

All jobs except pushing to Docker Hub are triggered if you have a pull request to the main on a selected branch.

We push to Docker Hub if and only if we merge.

# How to run an app?

Run in terminal: `$ poetry run uvicorn src.app:app --port <port>`

# How to run tests?
### How to run all tests?
Run in terminal: `$ poetry run pytest`
### How to run unit tests?
Run in terminal: `$ poetry run pytest tests/unit`
### How to run integration tests?
Run in terminal: `$ poetry run pytest tests/integration`

# How to check test coverage?

Run in terminal: `$ poetry run pytest --cov=src`

# How to pull this Docker image?

Run in terminal: `$ docker pull brutaljesus/devops_lab_2`

# How to build this Docker image?

Run in terminal: `$ docker build -t devops_lab_2 .`

# How to run this Docker image?

If you have pulled it: `$ docker run -p 8000:8000 brutaljesus/devops_lab_2`
Or if you have built it manually: `docker run -p 8000:8000 devops_lab_2`
