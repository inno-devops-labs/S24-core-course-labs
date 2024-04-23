# How to Work with This Web Application

![Workflow Status](https://github.com/Uzifam/S24-core-course-labs/actions/workflows/7980088734/badge.svg)

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


## Unit Tests
All `Unit tests` lie in directory `/app_python/tests/...`
Tests include static testing of code. 

## CI workflow
The code contains CI. After creating a pull request, instructions will be uploaded:

```
1)Unit test;
2)lint;
3)build & push a docker image
```


## API :
* `/` - return Moscow time;
* `/visits` - return number of visits

## Visits
The number of visits are saved in the visits.txt