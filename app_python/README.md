# Moscow Time Web App

This Python web application displays the current time in Moscow.

## Features

- Lightweight web app built with Flask.
- Utilizes `pytz` for accurate time zone handling.
- Follows PEP 8 coding standards for clean and readable code.
- Includes a simple unit test to ensure time format correctness.

## Setup

It is advisable to create a virtual environment before proceeding with the installation. [Refer to the guide here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and visit http://localhost:5000 to see the current time in Moscow.

## Setup via docker

### Build
Build the Docker Image: 
```bash
docker build -t app-flask .
```

### Pull and Run from Dockerhub
If you prefer to use a pre-built Docker image from Dockerhub. Pull the Docker Image:
```bash
docker pull blbr13/app-flask:lab2
```

### Run Container
Run the Docker Container:
```bash
docker run -d -p 5000:5000 app-flask
```

> After successfully building or pulling the Docker image and running the container, you can access the Flask application by navigating to http://localhost:5000 in your web browser.

## Unit Tests
Run the unit tests:
```bash
python -m unittest tests/test_app.py
```

## Dependencies
* Flask
* pytz
* pytest
