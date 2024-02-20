# 🇷🇺 Python web application for getting Moscow time

The main purpose of the application is to get current Moscow time in real time format.

## Structure

The project structure organized by using two important parts

1. Frontend (written using HTML and JavaScript)
2. Backend API (written using Python with FastAPI framework)

### Server's endpoints description

Server will be located on http://127.0.0.1:8000.

Detailed description of the server could be viewed using `/docs` endpoint.

Shortly it consist of two parts

1. `/` For getting html document with the main frontend.
2. `/api/time` For getting current moscow time up to seconds.

## Installation guide

To try our service simply you can use prepared Makefile.
Here are several commands to use

1. `make build` for creating python virtual environment and installing required dependencies.
2. `make run` for running application after installing dependencies (i.e. after using `make build`)
3. `make start` just union of two previous steps.
4. `make remove` Remove unistalled dependencies from the `make build` command.

## Docker

Except of custom installation we have also an option to install the application using docker containers.

### Build or Pull

We have several options to use docker container: either you can install our official image from the **docker hub** or build by
yourself.

#### How to build

After retrieving the source code go to the folder with `Dockerfile` and run next command:

`docker build -t {specify_name_for_the_container} .`

#### How to pull?
To pull our pre-built image you can use docker hub with next command:

`docker pull
tatarinalba/devops:1.0`

#### How to run?
To run the image you can use next command:

`docker run -d -p {your_port_number}:8000 -t tatarinalba/devops:1.0`

Tadam. It works!

## Unit Tests

In our application we also applied unit testing for improvement code quality.
* `test_api` - test verifies that correct Moscow time has been retrieved.

You can follow our test files for getting more information about usage of our program and expected output.

## CI Workflow
![CI workflow](https://github.com/tatarinalba/S24-core-course-labs/actions/workflows/main.yml/badge.svg)

Our workflow triggers when we're pushing to the lab3 branch.
We have several steps during our workflow.
- Dependencies installation
- Linting
- Testing
- Docker hub deploying