# Web Application that displays the current Moscow time

[![Python App Workflow](https://github.com/sapushha/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)](https://github.com/sapushha/S24-core-course-labs/actions/workflows/main.yaml)

## How to run

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:

    ```bash
    python app_python/app.py
    ```

3. Open the web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the current time in
   Moscow.

## How to Test

```bash
pytest app_python/unittests.py
```

## Running the Docker image

1. Pull the Docker image from Docker Hub:

    ```bash
    docker pull sapushha/sapushha_flask_app
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8080:8080 sapushha/sapushha_flask_app
    ```

## Building the Docker Image

1. Change the current directory to `app_python`:

    ```bash
    cd app_python
    ```

2. Build the Docker image:

    ```bash
    docker build -t sapushha_flask_app .
    ```

## Github Actions Workflow

### Workflow Name

Python App Workflow

### Triggers

push: The workflow is triggered when a push event occurs in the repository.

pull_request: The workflow is triggered when a pull request is opened or updated.

### Permissions

The workflow requires read access to the contents of the repository.

### Jobs

python-app-job: This job runs on the latest version of the Ubuntu operating system.

### Steps

Lint: It runs the Pylint tool to perform static code analysis on the app.py file.

Test: The workflow runs the unit tests for the application using the pytest framework by executing the pytest unittests.py command.

Snyk Run: The workflow runs the Snyk test to check for security vulnerabilities in the application, using the snyk test command and providing the Snyk token from the repository secrets.
