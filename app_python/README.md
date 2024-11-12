# Python application

## Overview
This is a simple python-based server that returns current time in the ```Europe/Moscow``` timezone.

## Installation

* Clone this repository to your machine
```bash
git clone https://github.com/geffk2/S24-core-course-labs.git -b lab1
```

* Create a venv and install required dependencies:
```bash
cd S24-core-course-labs
make
```
OR
```bash
cd S24-core-course-labs
python3 -m venv app_python/venv
source app_python/venv/activate
pip3 install -Ur app_python/requirements.txt
```

* Run the server(by default listens on all interfaces on port 8080):
```bash
make run
```
OR
```bash
source app_python/venv/activate
python3 -m app_python
```

* Test for correct output:
```console
foo@bar:~$ curl localhost:8080
2024-02-05 19:21:56.513728+03:00⏎
```

## Unit tests
This project utilises unit tests with the use of `pytest`.
To run tests use `make test`

## CI
This project utilises github actions CI to:
- Lint and test the project
- Build and push a docker image
On push(to any branch, not just main for ease of testing)
