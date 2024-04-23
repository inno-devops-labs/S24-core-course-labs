# Moscow Time Web App
[![Python CI](https://github.com/glebuben/S24-core-course-labs/actions/workflows/CI.yml/badge.svg)](https://github.com/glebuben/S24-core-course-labs/actions/workflows/CI.yml)

This is a simple Flask web application that displays the current time in Moscow. It provides a basic user interface to view the current time in the Moscow timezone.

## Features

- Displays the current time in Moscow timezone.
- Keeps track of the number of visits.
- Built with Flask, a simple and flexible Python web framework.

## Manual Set Up
### Installation
1. Clone the repository:

    ```
    git clone https://github.com/glebuben/S24-core-course-labs.git
    ```

2. Navigate to the project directory:

    ```
    cd S24-core-course-labs/app_python
    ```

3. Install dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask application:

    ```
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to view the current time in Moscow.

## Set Up via Docker
### Getting Image
There are 2 possible ways to get the image for this app:
1. Build it via 'Dockerfile'
    ```
    docker build -t <image name> app_python/
    ```

2. Pull from Dockerhub
    ```
    docker pull glebuben/dev-ops-labs:1.0
    ```
   **Note: the image name in the second case is "glebuben/dev-ops-labs:1.0"**

### Running the Image
To run the image, use this command line:

    ```
    docker run -d -p 5000:5000 <image name>
    ```
## Endpoints

### `/`
- **Description**: Displays the current time in Moscow timezone.
- **Method**: GET
- **Usage**: Open your web browser and go to [http://localhost:5000](http://localhost:5000).

### `/visits`
- **Description**: Displays the total number of visits to the application.
- **Method**: GET
- **Usage**: Open your web browser and go to [http://localhost:5000/visits](http://localhost:5000/visits).

## Unit Tests

For ensuring the correctness and reliability of the application, unit tests have been implemented. These tests verify the functionality of key components and features of the Flask web app.

### Usage

1. Navigate to the `tests` directory:

    ```
    cd tests
    ```

2. Run the unit tests:

    ```
    python test_app.py
    ```

### Test Structure

The unit tests are structured into separate test cases, each focusing on specific functionalities of the Flask web app. Here's an overview of the test cases and their respective functionalities:

- **Test Time Accuracy**: Validates the accuracy of the time retrieved by the `get_moscow_time` function against the actual time in the Europe/Moscow timezone.

- **Test Time Format**: Verifies the format of the time string returned by the `formatted_time` function.

- **Test Display Moscow Time**: Ensures that the `display_moscow_time` route returns a valid response.

- **Test Visit Counter**: Tests the functionality of the visit counter.

## Dependencies

Ensure the following dependencies are installed before running the unit tests:

- Flask
- pytz

## Continuous Integration Workflow

The CI workflow defined in this project automates the testing, linting, and Docker image building process for the Python application using GitHub Actions. The workflow consists of the following jobs:

### Build and Test
- **Job Name**: build_test
- **Trigger**: Triggered on every push to the repository.
- **Description**: This job sets up a Python environment, caches dependencies to speed up subsequent runs, installs project dependencies, and runs unit tests using `unittest`.

### Linting
- **Job Name**: lint
- **Trigger**: Triggered on every push to the repository.
- **Description**: This job checks the code for style and potential issues using Flake8, a Python linting tool. It ensures that the codebase adheres to coding standards and best practices.

### Docker Image Building
- **Job Name**: docker
- **Trigger**: Triggered on every push to the repository.
- **Description**: This job builds and pushes a Docker image of the Python application to Docker Hub. It sets up Docker Buildx for multi-platform builds and utilizes Docker's official actions for seamless integration.

The CI workflow helps maintain code quality, ensures consistency, and automates the deployment process, facilitating efficient development practices.

Update it according to the changes made.
