# Python Sample Application

## Overview

This is a simple python web application that shows current time in Moscow.

## Installation

- Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/dmfrpro/S24-core-course-labs -b lab1
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
```

## Docker

### Build

```bash
cd S24-core-course-labs/app_python
docker build --tag your_docker_username/app_python:v1.0 .
```

### Pull and Run

```bash
docker pull dmfrpro/app_python:v1.0
docker run -p 8080:8080 dmfrpro/app_python:v1.0
```

- Run the application and test:

```bash
python3 app.py
curl localhost:5000
```
