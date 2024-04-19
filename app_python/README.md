# Python Sample Application

![workflow](https://github.com/dmfrpro/s24-core-course-labs/actions/workflows/app_python.yaml/badge.svg)

## Overview

This is a simple python web application that shows current time in Moscow.
Also supports `/visits` endpoint returning `{"visits": N}` JSON.

## Installation

- Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/dmfrpro/S24-core-course-labs
cd S24-core-course-labs/app_python
```

- Install virtual environment and dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

- Run the application (via `gunicorn`) and test:

```bash
python3 -m gunicorn --bind 0.0.0.0:8080 app:app
curl localhost:8080
curl localhost:8080/visits
```

## Docker

### Build

```bash
cd S24-core-course-labs/app_python
docker build \
   --tag $(whoami)/app_python:v1.1 \
   --build-arg UID=10001 \
   --build-arg GID=10001 .
```

### Pull and Run

```bash
docker pull dmfrpro/app_python:latest
docker run -p 8080:8080 dmfrpro/app_python:latest
```

## CI Workflow

### Setup

1. CI starts with linting using `black` linter (`lint` job)
2. Then it installs dependencied and run `pytest` (`test` job)

### SNYK

After two jobs above completed, `snyk_check` job runs

### Building Docker image & Deploying

1. First of all the job starts with logging into Dockerhub using
   `DOCKER_USERNAME` and `DOCKER_TOKEN` repo secrets
2. Then it builds and pushes an image to Dockerhub
3. Build is cached in order to optimize future pipelines
