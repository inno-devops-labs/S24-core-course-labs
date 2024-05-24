# MSK time

![CI workflow](https://github.com/rinri-d/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)

A python web app that shows current server time in Moscow timezone.

## Usage

Set up a virtual environment and execute these commands:

```bash
pip install -r requirements.txt
cd src
uvicorn main:app --reload
```

## Docker
You can run the app using docker.

### Build
```bash
docker build -t python-test-app_python .
```

Alternatively, you can pull the image from docker hub:
```bash
docker pull rinri/python-test-app_python
```

### Run
```bash
docker run -p 8000:8000 rinri/python-test-app_python:latest
```

### CI workflow
The CI workflow of this repository tests the app using pytest, lint using ruff, builds the docker image, and finally pushes it to [Docker Hub](https://hub.docker.com/r/rinri/python-test-app_python). There is also SNYK vulnerability check, but it doesn't work.

