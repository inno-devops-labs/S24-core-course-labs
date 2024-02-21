# Go Web Application Documentation

## Overview

This Go web application is designed to display the current time in Moscow. It provides a simple and intuitive interface for users to view the current time in the specified timezone.

## Building manually

```bash
go build
```

## Docker: Using Containerized Application

This Golang application has been containerized using Docker for improved portability and ease of deployment.

### Building manually

To build the Docker image for the FastAPI application, run the following inside root dir of the project:

```bash
docker build -t app_go-lab2 .
docker run -p 8000:8000 app_go-lab2
```

The application now will be accessible at http://127.0.0.1:8000

### Pulling the Docker Image

If you prefer to pull the Docker image from Docker Hub, follow these steps:

```bash
docker pull tsepanx/app_go-lab2
docker run -p 8000:8000 tsepanx/app_go-lab2
```

The application now will be accessible at http://127.0.0.1:8000