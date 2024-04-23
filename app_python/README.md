# Moscow Time Application

[![CI](https://github.com/blinikar/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)](https://github.com/blinikar/S24-core-course-labs/actions/workflows/main.yaml)

## Overview

This application make opportunity to see the current moscow time in your web browser.

## Development & Deploy

All this instruction are suitable for MacOS.

1. Install the requirements

```
python3 install -r requirements.txt
```

2. Start the application 

```
python3 -m gunicorn --bind 0.0.0.0:8080 app:app
curl localhost:8080
curl localhost:8080/visits
```
You can find your application at http://localhost:5000


## Testing

Run following command to test the application: 

```
python -m unittest test.py
```

## Docker

### Containerized Application
This application is containerized using Docker for easy deployment and portability. The Docker image contains all the necessary dependencies to run the Python application.

### Instructions for Execution

#### Build Docker Image
To build the Docker image for this application, follow these steps:
```
bash
docker build --tag devops-app --build-arg UID=10001 --build-arg GID=10001
```

#### Pull Docker Image
To pull the Docker image from Docker Hub, run the following command:
```
bash
docker pull blinikar/devops-app
```

#### Run Docker Container
To run the Docker container with the application, use the following command:
```
bash
docker run -d -p 5000:5000 devops-app
```

The application will be accessible at http://localhost:5000.

