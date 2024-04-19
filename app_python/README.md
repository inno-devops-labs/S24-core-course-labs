![CI Workflow](https://github.com/y0szx/devops/actions/workflows/main.yml/badge.svg)

# Current Moscow time web application documentation

## Overview

This is a simple Python web application built using Flask. Its main feature is to display the current time in Moscow.

## Prerequisites

Make sure you have Python and Docker installed on your system.

## Local installation

* Clone the repository to your local machine:

```bash
git clone https://github.com/y0szx/devops.git
```

* Go to the `app_python`:

```bash
cd app_python
```

* Create virtual environment:

```bash
python3.11 -m venv env
source env/bin/activate
```

* Install dependencies:

```bash
pip install -r requirements.txt
```

* Run the application:

```bash
python main.py 
```

* Go to https://127.0.0.1:5000 to view the result.

## Docker

This application is containerized using Docker to ensure consistency and portability across different environments. The
Docker image includes all the necessary dependencies to run the application.

* ### How to build?

To build image locally go to app_python directory and use:

```bash
docker build -t app_python .
```

To run locally use:

```bash
docker run -p 5000:5000 app_python
```

* ### How to pull?

To pull the image from the Docker Hub use:

```bash
docker pull yuszx/app_python
```

* ### How to run?

To run pulled image use:

```bash
docker run -p 5000:5000 yuszx/app_python
```

Go to https://127.0.0.1:5000 to see the result.

## Unit Tests

* `test_response`: checks if respond is successful when request is made
* `test_time_format`: checks if returned time is in the expected format

You can read the full description by referring to `PYTHON.md`.

## CI workflow

This repository is configured with a continuous integration (CI) workflow using GitHub Actions. The CI workflow includes
three jobs:

### 1. Build

* Checkout repository
* Set up Python environment (using Python 3.11)
* Install snyk
* Cache dependencies to speed up subsequent runs
* Install dependencies from requirements.txt
* Run tests
* Linting with flake8

### 2. Security

* Runs only after successful building
* Check vulnerabilities using snyk

### 3. Docker

* Login into Docker hub
* Set up Buildx
* Build and push image

These CI workflows help ensure the quality and reliability of the Python package and Docker image associated with this
repository.

## Counter logic

This application can show the number of times it was accessed by implemented counter logic. To see this, first execute
`docker-compose build` in `app_python` folder, then run `docker-compose run`, navigate to `localhost:5000/visits` and
here you can see the number of times this application was accessed. Counter saves this number even after stopping
application by saving the number in `visits/visits.txt`.
