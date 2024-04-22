# Flask Web Application Documentation

## Overview

This simple Flask web application displays the current time in Moscow.
The application is built using the Flask framework and utilizes
the datetime module for handling time and the pytz library for
handling time zones.

`/visits` route is used for number of total visits on this app 

## Flask Installation

1. Ensure you have Python installed on your system. You can download it from `python.org`.

2. Install Flask using the following command:

    ```bash
    pip install flask
    ```

   Make sure to use a virtual environment for better isolation.
3. Install pytz using the following command:

    ```bash
    pip install pytz
    ```

## Flask Usage

1. Run the Flask application by executing the following command in the terminal:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://localhost:5000/` to view the current time in Moscow.

## Docker Installation

1. Install docker desktop from [official website](https://www.docker.com/products/docker-desktop/)

2. Run docker desktop

## Docker usage

Run commands from `app_python` directory

### Local run

1. Build stage

   ```bash
   cd app_python
   docker-compose build
   ```

2. Run stage

   ```bash
   docker-compose up
   ```

3. Open <http://localhost:5080/> and see the result

### Remote run

1. Pull stage

   ```bash
   docker pull doechon/app_python
   ```

2. Run stage

   ```bash
   docker run -d -p 5000:5000 doechon/app_python
   ```

3. Open <http://localhost:5000/> and see the result

## Unit Tests

The unit tests are designed to validate the functionality of the Flask web application that displays the current time in Moscow. Two main test cases are implemented:

1. `test_display_moscow_time`: Checks if the application displays the current time in Moscow correctly.
2. `test_invalid_route`: Checks if the application returns a 404 status code for an invalid route.

## CI Workflow

This project includes a continuous integration (CI) workflow to automate testing and Docker image building. The workflow is triggered on each push to the repository. Here's what the CI workflow does:

1. Checks out the repository code.
2. Sets up Python environment with version 3.9.
3. Installs project dependencies specified in app_python/requirements.txt.
4. Lints the code using Flake8.
5. Runs unit tests.
6. Checks for vulnerabilities in dependencies using Snyk.
7. Logs in to Docker Hub.
8. Builds a Docker image for the application.
9. Pushes the Docker image to Docker Hub.

## Dependencies

* Flask
* datetime
* pytz
* Docker
