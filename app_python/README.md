# Python App

![Bun](https://github.com/pptx704/S24-devops-labs/actions/workflows/build-bun.yaml/badge.svg)

This is a simple web application that displays the current time in Moscow. The application is developed using Python and Flask framework.

![Screenshot](https://i.postimg.cc/XYVk7s95/image.png)

## Table of Contents

- [Python App](#python-app)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation Steps](#installation-steps)
    - [Docker](#docker)
  - [Development](#development)
    - [Unit Tests](#unit-tests)
    - [CI Workflow](#ci-workflow)

## Installation

### Requirements

- Python 3.8 or higher
- `pip` package manager

### Installation Steps

- Clone this branch to your local machine

```bash
git clone git@github.com:pptx704/S24-devops-labs -b lab1
```

- Navigate to the `app_python` folder

```bash
cd app_python
```

- Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the required packages

```bash
pip install -r requirements.txt
```

- Run the application

```bash
flask run
```

The application will be available at [localhost:5000](http://localhost:5000/)

### Docker

It is possible to either build the Docker image from the Dockerfile or pull the image from the Docker Hub.

To build the image, use the following command:

```bash
docker build -t app_python .
```

To pull the image from the Docker Hub, use the following command:

```bash
docker pull pptx704/app_python:latest
```

After building or pulling the image, the container can be run with the following command:

```bash
docker run -p 5000:5000 app_python
```

The application will be available at [localhost:5000](http://localhost:5000/)

In `/` endpoint, it will show the current time in Moscow-

![Example](https://i.postimg.cc/XYVk7s95/image.png)

In `/visits` endpoint, it will show the number of visits to the `/` endpoint.

![Visits](https://i.postimg.cc/fR8rBbKK/image.png)

## Development

Contributions are not accepted at the moment as this is just a lab assignment. You can fork the repository for your own use.

### Unit Tests

Unit tests are maintained in the `test.py` file. To run the tests, use the following command:

```bash
python -m unittest app_python/test.py # Make sure that you are in the parent directory of app_python
```

To check the code coverage, use the following command:

```bash
coverage run -m unittest app_python/test.py
coverage report
```

### CI Workflow

A CI workflow is maintained in the `.github/workflows/build-python.yaml` file. This workflow lints and tests the application, checks code vulnerability using SNYK, and builds and pushes docker image. Workflow is triggered only if the there is a change in the `app_python` directory or the workflow file itself.

The CI workflow contains 3 jobs. Each job has a specific set of tasks to perform:

- Build: This job lints and tests the application
- Security: This job checks code vulnerability using SNYK
- Docker: This job builds and pushes the docker image to the Docker Hub. The job is carried out only if the previous jobs are successful.

More details about the CI workflow can be found in the [CI.md](CI.md) file.
