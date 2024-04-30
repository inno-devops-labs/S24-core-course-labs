# Flask Web Application 

[![flask-app](https://github.com/VectorsMaster/S24-core-course-labs/actions/workflows/main.yaml/badge.svg?branch=lab3)](https://github.com/VectorsMaster/S24-core-course-labs/actions/workflows/main.yaml)

## Overview

This is a flask web application that renders current time in Moscow zone in the home page `host_url/` and renders number of visits to the home page in `host_url/visits`

## Steps to run the application 

1. Install `Python 3`.

2. Navigate to `app_python` directory.

3. Set up virtual environment.
    - On Windows: `python -m venv venv`.
    - On Unix-based systems: `python3 -m venv venv`.

4. Activate the virtual environment.
    - On Windows: `.\venv\Scripts\activate`.
    - On Unix-based systems: `source venv/bin/activate`.

4. install requirements `pip install -r requirements.txt`.

5. Run `flask --app flaskr/app run`.

## Steps to test the app on Unit Tests

1. Navigate to `app_python` directory.

2. Set up virtual environment, activate it and install requirements as mentioned previously.

3. Run `pytest`.

There exists 3 Unit tests:

1. Test to check whether the app is responding to get requests
2. Test to chech whether the app is rendering time block
3. Test to check whether time changes upon refreshing (subsequent requests)

## Steps to build docker  

1. navigate to `app_python` directory. 

2. run `docker build -t name .`

## Steps to run docker  

- run `docker run -p 5000:5000 name`

## Steps to push the docker image

1. `docker login`
2. `docker tag name yourusername/name`
3. `docker push yourusername/name`

## Steps to pull and run the docker image
1. `docker pull yourusername/name`
2. `docker run -p 5000:5000 yourusername/name`

## Steps to run docker-compose
```docker-compose
version: '3'

services:
  web:
    image: yourusername/flask-app
    ports:
      - "5000:5000"
    volumes:
      - ./visits.txt:/app_python/visits.txt
```
1. `docker compose pull`
2. `docker compose up`

In this Docker Compose configuration, the purpose of the "volumes" section is to create a persistent data storage mechanism for the container. Specifically, it binds the local directory ./visits.txt to the directory /app-python/visits.txt inside the container, in order to see the number of visits on the host machine. So make sure this file exists before running `docker compose up`.

## CI workflow
This project is set up with continuous integration (CI) using GitHub Actions. The CI workflow performs the following steps on every push:

1. **Dependencies:** Installs project dependencies using `pip`.
2. **Linting:** Runs linting checks using `flake8` to ensure code quality.
3. **Tests:** Runs automated tests using `pytest`.
4. **Docker:** Builds a Docker image and pushes it to Docker Hub.
5. **Snyk:** runs the Snyk test to check for vulnerabilities in the Python dependencies.

You can also run these steps locally by following the instructions in the [CI Workflow](/.github/workflows/main.yml) file.

**Make sure you add Docker Hub Credentials and Snyk token as Secrets**
   - Navigate to your repository on GitHub.
   - Go to `Settings` > `Secrets`.
   - Click on `New repository secret`.
   - Add your Docker Hub username, password, and snyk tokek as secrets with the names `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `SNYK_TOKEN` respectively.

These secrets will be securely accessed by GitHub Actions during the Docker-related steps of the CI workflow.
