# App Python
[![Workflow Status](https://github.com/LaithAlebrahim/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)](https://github.com/LaithAlebrahim/S24-core-course-labs/actions/workflows/main.yaml)

This repository contains a Flask-based web application designed to display the current time in Moscow. It serves as an example of implementing best practices in web application development with Python.


## Overview

The application is straightforward, with its primary function being to show the current Moscow time to the user. This functionality is implemented using the Flask framework and the `pytz` library for accurate timezone handling.

## Local Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:
```bash
git clone https://github.com/LaithAlebrahim/S24-core-course-labs.git
```
## Usage

To use this application, run the following commands:

```bash
cd app_python
```

2. **Install Dependencies**:
```bash
pip3 install -r requirements.txt
```
3. **Run the Application**:
```bash
python3 app.py
```
4. **View in Browser**:
Open your browser to http://localhost:5000/ to see WEB APP


## Unit Tests
Run the unit tests:
```bash
python -m unittest tests/test_app.py
```

### Build and Test Job
- Set up Python, install project dependencies and run tests using `pytest`.


## Docker Container
To simplify deployment, the application has been containerized with Docker. Follow these steps to run the app using Docker:
1. **Build the Docker Image locallu:**:
```bash
docker build -t AlebrahimLaith/app_python:latest .
```
2. **Run the Docker Container:**:
```bash
docker run -p 5000:5000 AlebrahimLaith/app_python:latest
```
3. **Access the application:**:
Open a browser and go to http://localhost:5000/ to view the application.

Or

2. **Pull the Docker image directly from Docker Hub:**
  ```bash
    docker pull AlebrahimLaith/app_python:latest

    docker run -d -p 5000:5000 AlebrahimLaith/app_python:latest
  ```
2. **Run the Docker Container:**:
```bash
docker run -p 5000:5000 AlebrahimLaith/app_python:latest
```
Open a browser and go to http://localhost:5000/ to view the application.

