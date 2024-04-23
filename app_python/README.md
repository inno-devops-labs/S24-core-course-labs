# Flask Web Application: Moscow Time Display

![workflow](https://github.com/IlyaPechersky/S24-core-course-labs/.github/workflows/main.yml/badge.svg)

This Flask web application displays the current time in Moscow on the main page. The time is updated every time the page is refreshed.

The project was created as the first laboratory work of the Devops course.

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.x
- pip package manager

### Installation Steps

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd app_python
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open a web browser and go to `http://127.0.0.1:5000/` to view the application.

### Deployment via docker

1. To build image locally use the following command from app_python dir:

    ```bash
    docker build . --tag app_python
    ```

2. To verify the image is built run:

    ```bash
    docker images
    ```

    You will get something like:
    ```console
    REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
    app_python   latest    87d2f7f96999   About a minute ago   1.03GB
    ```

3. You can also pull the image from dockerhub:

    ```bash
    docker pull happystove/app_python:1.0
    ```

4. To run:
    
    ```bash
    docker run app_python
    ```

    Or if you use dockerhub:

    ```bash
    docker run happystove/app_python:1.0
    ```

## Files Overview

- `app.py`: Contains the Flask application code, including route definitions and the function to retrieve Moscow time.
- `templates/`: Contains HTML templates.
- `test.py`: Contains unit tests for the Flask application.
- `requirements.txt`: Lists the dependencies required for the project.
- `PYTHON.md`: Describes the reason for choosing the framework, best practices, and implementation details.
- `README.md`: Provides an overview of the project, installation instructions, and file descriptions.

## Endpoints

- `/`: Home page shows current time in Moscow
- `/visits`:  Visits page show recorded visits

## Usage

Once the Flask application is running locally, open a web browser and navigate to `http://127.0.0.1:5000/` to view the application. The main page will display the current time in Moscow, which will be updated every time the page is refreshed.

## Unit Tests

- `test_index_route`: Checking the main sections for HTML.
- `test_get_moscow_time_format`: Checking the format of the returned time.
- `test_index_template_rendering`: It mocks the returned time, and then sends it to the HTML page, check that this time is displayed.

You can read about the implemented best practices at [PYTHON.md](PYTHON.md).

## CI workflow

This GitHub Actions workflow automates the testing, linting, and Docker image building process for a Python application.

## Trigger
The workflow runs on every push event.

## Jobs

### Test
- **Runs on:** Ubuntu latest
- **Steps:**
  - Checks out the codebase
  - Sets up Python version 3.12
  - Installs dependencies from `requirements.txt`
  - Lints code using Flake8
  - Executes tests with `pytest`
  - Checks vulnerabilites using SNYK

### Docker Hub Credentials
The workflow requires Docker Hub credentials to push the Docker image. Make sure to set up the `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets in your repository settings.

### Build and Push Docker Image
- **Runs on:** Ubuntu latest
- **Steps:**
  - Sets up Docker Buildx
  - Logs in to Docker Hub using provided credentials
  - Builds and pushes the Docker image tagged as `user/app:latest`


## License

[License information, if applicable]


