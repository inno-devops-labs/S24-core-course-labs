# Flask Web Application displaying current time in Moscow

[![Test](https://github.com/plov-cyber/S24-core-course-labs/actions/workflows/test.yml/badge.svg?branch=lab-3&event=push)](https://github.com/plov-cyber/S24-core-course-labs/actions/workflows/test.yml)
[![Lint](https://github.com/plov-cyber/S24-core-course-labs/actions/workflows/lint.yml/badge.svg?branch=lab-3&event=push)](https://github.com/plov-cyber/S24-core-course-labs/actions/workflows/lint.yml)

## Description

This is a simple Flask web application that displays the current time in Moscow.

## Structure

- `app.py` - the main application file.
- `requirements.txt` - the list of required Python packages.
- `templates` - the directory containing HTML templates.
    - `base.html` - the base HTML template.
    - `moscow_time.html` - the template for the main page.
- `static` - the directory containing static files.
    - `style.css` - the CSS file for the application.
- `tests` - the directory containing tests.
    - `unit` - the directory containing unit tests.
        - `test_moscow_time.py` - the unit test for the application.

## How to Run

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

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests:

    ```bash
    python app_python/tests/unit/test_moscow_time.py
    ```

## Using Docker

1. Pull the Docker image from Docker Hub:

    ```bash
    docker pull rekhlov/devops-flask-app
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8080:8080 rekhlov/devops-flask-app
    ```

3. Open the web browser and navigate to [http://127.0.0.1:8080/](http://127.0.0.1:8080/) to see the current time in
   Moscow.

### Building the Docker Image

1. Change the current directory to `app_python`:

    ```bash
    cd app_python
    ```

2. Build the Docker image:

    ```bash
    docker build -t devops-flask-app .
    ```

## CI Workflow

The CI workflow is set up using GitHub Actions. There are two workflows: **Lint** and **Test**.

### Lint Workflow

The Lint workflow checks the code for any linting issues using `pylint`.

The workflow is triggered on every push & pull request in the repository.

### Test Workflow

The Test workflow runs the unit tests for the application.

The workflow is triggered on every push & pull request in the repository.

## Author

Created by Lev Rekhlov, B21-DS-02, [l.rekhlov@innopolis.university](mailto:l.rekhlov@innopolis.university)
