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

## Visits page

Count of visits to the main page can be accessible via `/visits` path.
This number is get incremented on every new visit and is saved to `visits/n` file (via docker volume)

Now app will be accessible at http://127.0.0.1:8000/

## Testing

Comprehensive unit tests have been implemented to ensure the reliability and correctness of the application's functionality.

Running tests:

```bash
pytest .
```

## Docker: Using Containerized Application

The FastAPI application has been containerized using Docker for improved portability and ease of deployment.

### Building manually

To build the Docker image for the FastAPI application, run the following inside root dir of the project:

```bash
docker build -t app_python .
docker run -p 8000:8000 app_python
```

The application now will be accessible at http://127.0.0.1:8000

### Pulling the Docker Image

If you prefer to pull the Docker image from Docker Hub, follow these steps:

```bash
docker pull tsepanx/app_python
docker run -p 8000:8000 tsepanx/app_python
```


The application now will be accessible at http://127.0.0.1:8000

## Continuous Integration (CI) Workflow

The project includes a CI workflow using GitHub Actions to automate the build and testing process. The workflow consists of several essential steps:

- **Dependencies**: Ensure dependencies are installed using pip
- **Linting**: Check code quality and adherence to coding standards using linters
- **Tests**: Run comprehensive unit tests to verify the application's functionality

Additionally, Docker-related steps are handled in a separate CI workflow specifically for Docker:

- **Build & Push**: Automatically build Docker images and push them to Docker Hub

For more details, refer to the workflow files located in the `.github/workflows` directory
