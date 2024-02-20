## Workflow Status

![Python CI Workflow](https://github.com/starkda/S24-core-course-labs/actions/workflows/python_ci.yml/badge.svg?event=push)

# Python Web Application

This is a Python web application built using the Flask framework to display the current time in Moscow.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd project_folder
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python3 app.py
    ```

5. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Docker

Building the Docker Image

 ```bash
    docker build -t <image name> .
```

Pulling the docker Image

 ```bash
    docker pull djhovi/my-flask-app:latest

```

Running the docker Image

 ```bash
    docker run -p5000:5000 djhovi/my-flask-app:latest

```

## Unit Tests

Comprehensive unit tests have been implemented to ensure the reliability and functionality of the Flask web application.

To run the unit tests, execute the following command in your terminal(in root project folder):

```bash
python3 -m unittest discover -s app_python/src/tests -p "test_application.py"
```

## Workflow Steps

The CI workflow consists of the following steps:

- **Dependencies:** Install project dependencies.
- **Linting:** Run code linting checks using Flake8.
- **Tests:** Run automated tests to ensure code quality.
- **Run Snyk Test:** The Snyk test command is executed to scan the project for vulnerabilities.
- **Docker Login:** Authenticate with Docker Hub using a Docker access token.
- **Docker Build and Push:** Build a Docker image and push it to Docker Hub.

### Workflow Configuration

The workflow is configured using a YAML file named `ci.yml` located in the `.github/workflows` directory. This file
defines the sequence of steps to be executed during the CI process.

### Viewing Workflow Status

The status of the CI workflow can be viewed in the "Actions" tab of this repository. Successful workflow runs will be
indicated by a green checkmark, while failed runs will display a red 'X'. You can click on individual workflow runs to
view detailed logs and any errors or warnings encountered during the process.

### GitHub Secrets

To enable the CI workflow, the following GitHub repository secrets are required:

- `DOCKER_ACCESS_TOKEN`: Docker access token for authentication when pushing Docker images.
- `SNYK_TOKEN`: Needed to use Snyk.
