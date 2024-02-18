![Github Actions CI](https://github.com/majorro/devops-engineering-course/actions/workflows/app-python-ci.yml/badge.svg)

# Moscow Time Web Application

This is a simple web application that shows the current time in Moscow.

## Getting started locally

### Prerequisites

- Python 3.9+

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

The running app will be available at http://localhost:8000

## Getting started with Docker

### Prerequisites

- Docker

### Usage

Build the image:

```bash
docker build -t majorro/devops-engineering-course:python .
```

or pull it from Docker Hub:

```bash
docker pull majorro/devops-engineering-course:python
```

Run the container:

```bash
docker run -p 8000:8000 majorro/devops-engineering-course:python
```

The running app will be available at http://localhost:8000

## Unit tests

Run with:

```bash
pytest ./app_python
```

## CI

The CI workflow is defined in `.github/workflows/app-python-ci.yml`
It consists of two jobs:

1. Build, lint, run tests, run security checks
2. Build and push Docker image to Docker Hub

## Contact

- [Telegram](https://t.me/majorro228)
