# Time API

## Description

Simple FastApi-based web API that can give you current time in Moscow Standard Time timezone.

## Local setup

### Setup

Prepare the environment:

1. Create venv
2. Install the requirements: `pip install -r requirements-dev.txt`

### Launch

Then you can actually launch the app:

```sh
uvicorn app.main:app --reload
```

### Interact

Now you can interact with the app. To see the current time in Moscow, visit <http://localhost:8000/time/msk>

## Interactive documentation

To view auto-generated Swagger docs, visit <http://localhost:8000/docs>

## Docker

### Build

Run

```sh
docker build -t devops-py .
```

### Pull

Run

```sh
docker pull dirakon/devops-py:latest
```

### Run

Run (on host port 5000 as example)

```sh
docker run -p 5000:80 dirakon/devops-py:latest
```

## Unit tests

To run unit tests, do

```sh
pytest
```
