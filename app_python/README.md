# Python Web-app

## Overview

This Python web application is designed to display the current time in Moscow, utilizing the FastAPI framework. It provides a simple and intuitive interface for users to access the current time in the specified timezone.

## Installation & Running

To install and run the application locally, follow these steps:

Clone the repository to your local machine:

```bash
cd app_python/
pip install -r requirements.txt
```

Run with 
```bash
uvicorn main:app --reload
```

Now app will be accessible at http://127.0.0.1:8000/

## Testing

Running tests:

```bash
pytest .
```

## Docker: Using Containerized Application

The FastAPI application has been containerized using Docker for improved portability and ease of deployment.

### Building manually

To build the Docker image for the FastAPI application, run the following inside root dir of the project:

```bash
docker build -t app_python-lab2 .
docker run -p 8000:8000 app_python-lab2
```

The application now will be accessible at http://127.0.0.1:8000

### Pulling the Docker Image

If you prefer to pull the Docker image from Docker Hub, follow these steps:

```bash
docker pull tsepanx/app_python-lab2
docker run -p 8000:8000 tsepanx/app_python-lab2
```


The application now will be accessible at http://127.0.0.1:8000