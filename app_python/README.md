# Python Web Application

![python build workflow](https://github.com/Tufra/S24-core-course-labs/actions/workflows/build_python.yaml/badge.svg)

A Web Application that displays current time in Moscow based on Google NTP service (since the system may have incorrect time set)

## Installation and Running

```bash
 python -m venv venv
 ./venv/Scripts/activate
 pip install -r requirements.txt
 cd app
 sanic server:app
```

If everything goes well, you will see startup logs with message`Starting worker [...]`. You can now see html page with moscow time at `localhost:8000`

## Docker

### How to build

```bash
cd app_python
docker build -t tufra/moscow-time-app-python .
```

### How to pull

```bash
docker image pull tufra/moscow-time-app-python:0.0.1
```

### How to run

```bash
docker run -p 80:8080 -t tufra/moscow-time-app-python:0.0.1
```

Now you can see moscow time at `localhost`

## Unit tests

### Test cases

- `get("/")` returns `200` code
- `get("/")` and `get("/")` after 2 seconds return different bodies

### How to run

```bash
cd app_python
pytest
```

## CI

Repository has a workflow `build_python` with 2 jobs:

- `build`
    - `Install dependencies`
    - `Lint with Ruff`
    - `Test with Pytest`
    - `Snyk test`
- `docker`
  - `Login to Docker Hub` (using `docker/login-action@v3` and repository secrets)
  - `Set up Docker Buildx` (using `docker/setup-buildx-action@v3`)
  - `Build and push` (using `docker/build-push-action@v5` and repository secrets)
