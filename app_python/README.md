[![Python App CI](https://github.com/vladdan16/S24-core-course-labs/actions/workflows/app_python.yaml/badge.svg)](https://github.com/vladdan16/S24-core-course-labs/actions/workflows/app_python.yaml)

# Current Moscow Time - FastAPI Web Application

This is a simple Python web application developed using FastAPI. The application displays the current Moscow time in the browser and updates continuously.

## Getting Started

These instructions will get a copy of the project running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.6+
- pip

### Installation & Usage

Clone the repository to your machine

```shell
git clone git@github.com:vladdan16/S24-core-course-labs.git
```

Navigate into the project directory

```
cd S24-core-course-labs/app_python
```

Install the required modules

```shell
pip install -r requirements.txt
```

Start the server

```shell
uvicorn app:app --reload
```

Then open your browser and go to http://localhost:8000/ to see the current time in Moscow. 


## Unit Tests

This project also contains unit tests, that allow us to keep code maintainable.


To run the tests type the following command:

```shell
pytest
```

## Docker

It is also possible to run this application with Docker

To build this app you should have docker installed and running on your machine:

```shell
cd app_python
docker build -t vladdan16/app_python .
```

There is also a depoyed image on Docker Hub. You can pull it with command:

```shell
docker pull vladdan16/app_python
```

To run container:

```shell
docker run -p 8080:8000 vladdan16/app_python
```

Now you should be able to access application at `http://localhost:8080`

## CI

In this project I have a CI workflow that run Linter and tests. It is also uses Synk for security check and
builds and pushes Docker image to DockerHub.
