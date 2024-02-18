# Python Web Application for Moscow time display

![CI](https://github.com/Ozurexus/S24-DevOps-labs/workflows/CI/badge.svg)

## Set Up

1. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install the required dependencies:

   ```bash
    pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python src/app.py
   ```

4. Open your web browser and navigate to `http://
localhost:5000/` to view the application.

5. (Optional) Run the tests:

   ```bash
   python tests/app_test.py
   ```

## Docker

1. To build the Docker image run the following command in the terminal from the `app_python` directory with Dockerfile present:

   ```bash
   docker build -t my-flask-app .
   ```

2. To run the Docker image:

   ```bash
   docker run -p 5000:5000 my-flask-app
   ```

3. Alternatively, you can pull the Docker image from my [dockerhub repository](https://hub.docker.com/repository/docker/ozurexus/my-flask-app) using the following commands:

   ```bash
   docker login
   docker pull ozurexus/my-flask-app
   docker run -p 5000:5000 ozurexus/my-flask-app
   ```

## Unit Tests

1. To run the unit tests, navigate to the `app_python` directory and run the following command:

   ```bash
   python -m unittest
   ```

2. There are 3 tests in the `app_test.py` file. The first test checks if the home page returns a 200 status code. The second test checks if the home page contains the text "Moscow Time". The third test checks if the home page contains the text "Moscow Time" and the time is displayed in the correct format.

3. After all tests are run, the results will be displayed in the terminal.

## CI Workflow

1. The CI workflow is set up using GitHub Actions. The workflow is triggered on every push to branches Lab3 and main.

2. The workflow includes the following steps:
   - Dependencies: Install the required dependencies.
   - Linter: Check the code for any syntax errors.
   - Tests: Run the unit tests.
   - Docker Login: Log in to Docker Hub.
   - Docker Build & Push: Build the Docker image and push it to Docker Hub.

## Stack

- Python
- Flask
- HTML
