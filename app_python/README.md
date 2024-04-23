[![Python App Workflow](https://github.com/Skril3366/S24-core-course-labs/actions/workflows/python.yml/badge.svg)](https://github.com/Skril3366/S24-core-course-labs/actions/workflows/python.yml)

# Date and Time in Moscow

## Table of Content

<!--toc:start-->
- [Date and Time in Moscow](#date-and-time-in-moscow)
  - [Table of Content](#table-of-content)
  - [Overview](#overview)
  - [Running](#running)
    - [Using Docker](#using-docker)
    - [Using Docker Compose](#using-docker-compose)
    - [Locally](#locally)
  - [Unit Tests](#unit-tests)
  - [CI workflow](#ci-workflow)
    - [Checks Job](#checks-job)
    - [Build Job](#build-job)
<!--toc:end-->

## Overview

An app that displays Moscow date and time that should be agnostic to the
timezone of the environment it is run on.

Application is written in Python using Flask, see [PYTHON.md](./PYTHON.md) for
more details

## Running

### Using Docker

You may use already built image:

```sh
docker pull skril/moscow-time:python
docker run -p 8080:8080 skril/moscow-time:python
```

Or build it yourself:

```sh
docker build -t moscow-time .
docker run -p 8080:8080 moscow-time
```

Now an app can be accessed at http://localhost:8080 and number of visits can be
seen at http://localhost:8080/visits

### Using Docker Compose

The simplest way to run the app is to:

```sh
docker compose up
```

### Locally

Requirements:

- `Python 3.11.6`

Install dependencies

```bash
poetry install
```

And then run application

```bash
poetry run python app/__init__.py
```

It can be accessed on http://localhost:8080/

## Unit Tests

Running unit tests

```bash
poetry run pytest
```

For more information about unit tests please refer to the corresponding section
of [PYTHON.md](./PYTHON.md)

## CI workflow

This GitHub Actions workflow automates testing and building of your Python
application. It's triggered whenever code changes in `app_python` directory are
pushed.

### Checks Job

The **Checks** job ensures the project passes basic quality checks on every commit by running tests and linting:

1. Clones the repository using the latest Ubuntu environment.
2. Installs Python version 3.11.6.
3. Uses Poetry package manager to manage dependencies and create a virtual environment.
4. Installs all required packages from the `pyproject.toml` file.
5. Performs static analysis using Flake8 with a complexity limit of 10.
6. Executes unit tests using PyTest.

### Build Job

After successful checks, the **Build** job builds and pushes a Docker image to Docker Hub:

1. Sets up Docker Buildx for multi-architecture support.
2. Logins into Docker Hub using secure credentials stored as secrets.
3. Builds and pushes an optimized Docker image based on the provided `Dockerfile`. The tag will be set to `skril/moscow-time:python`.
