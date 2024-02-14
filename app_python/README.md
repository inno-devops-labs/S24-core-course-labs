# How to Work with This Web Application

## Starting the Web Service

To start the web service, follow these steps:

1. Fill in the environment variables that should be in `~/app_python/.env`.
2. Build and run the Docker container using the following commands:


# DOCKER
## How to build:
```bash
docker build -t flask-app .
```
## How to pull ?
```bash
docker pull flask-app
```
## How to run ?
```bash
docker run -d -p {port-name}:{docker-port-name} --name new_container flask-app
```

## How to check
Go to the `localhost:{port-name}`