# Flask Web Application

[![App Python Testing](https://github.com/AlmetovKamil/S24-core-course-labs/actions/workflows/app_python_testing.yaml/badge.svg?branch=lab3&event=push)](https://github.com/AlmetovKamil/S24-core-course-labs/actions/workflows/app_python_testing.yaml)

[![App Python Docker Build and Push](https://github.com/AlmetovKamil/S24-core-course-labs/actions/workflows/app_python_docker_push.yaml/badge.svg?branch=lab3&event=push)](https://github.com/AlmetovKamil/S24-core-course-labs/actions/workflows/app_python_docker_push.yaml)

This is a simple Flask web application that displays the current Moscow time. It provides a basic example of how to create a web application using the Flask framework.

## Features

- Displays the current Moscow time on the homepage.
- Utilizes Flask framework for routing and rendering templates.
- Implements basic error handling for invalid routes.
- Implements visits: counts how many times a user accessed the app and displays that number in the /visits folder

## Getting Started

To get a local copy of this project up and running, follow these steps:

### Prerequisites

- Python 3 installed on your local machine.
- pip package manager installed.

### Installation

1. Clone the repository to your local machine:

2. Activate venv

3. Install requirements

### Usage

1. Run the Flask application

2. Open a web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the web application.

## Docker

### Building the Docker Image

To build the Docker image locally, follow these steps:

1. Ensure that Docker is installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the root directory of the cloned repository.
4. Run the following command to build the Docker image:
   ```bash
   docker build -t app_python .
   ```

### Pulling the Docker Image

If you prefer to pull the Docker image from Docker Hub instead of building it locally, you can use the following command:

```bash
docker pull almetovkamil/app_python:v2
```

### Running the Docker Container

Once you have the Docker image, you can run the container using the following command:

```bash
docker run -d -p 5000:5000 almetovkamil/app_python:v2
```
This command will run the container in detached mode (`-d`) and map port 5000 on the host to port 5000 in the container.

You can now access your application by navigating to `http://localhost:5000` in your web browser.

## Unit Tests

We have implemented unit tests to ensure the correctness and reliability of our code. These tests cover critical components of our application and help us catch bugs early in the development process.

To run the unit tests locally, follow these steps:

1. Ensure that Python and the necessary dependencies are installed on your system.
2. Navigate to the root directory of the project.
3. Run the following command to execute the unit tests:
   ```bash
   pytest
   ```

## Continuous Integration (CI) Workflow

### GitHub Actions

We have set up a CI workflow using GitHub Actions to automate the testing, linting, building, and pushing of our application Docker image to Docker Hub.

#### Linter and Testing Workflow

The `linter` job is responsible for setting up dependencies, running linting checks, and testing our application code. It consists of the following steps:

1. **Checkout**: Check out the code from the repository.
2. **Install Dependencies**: Install Python dependencies specified in `requirements.txt`.
3. **Lint with Ruff**: Run linting checks using Ruff.
4. **Test with pytest**: Run unit tests using pytest.

The job runs on each push event to the repository.

#### Docker Build and Push Workflow

The `build` job is responsible for building the Docker image of our application and pushing it to Docker Hub. It consists of the following steps:

1. **Checkout**: Check out the code from the repository.
2. **Login to Docker Hub**: Authenticate with Docker Hub using Docker login.
3. **Set up Docker Buildx**: Set up Docker Buildx for building multi-platform Docker images.
4. **Build and push**: Build the Docker image using the Dockerfile located in the `app_python` directory and push it to Docker Hub with the specified tags.

The job also runs on each push event to the repository.

### How to Use the CI Workflow

1. **Push to Repository**: Make changes to your code and push them to your GitHub repository.
2. **GitHub Actions**: GitHub Actions will automatically trigger the CI workflow defined in the `.github/workflows` directory.
3. **View Results**: You can view the workflow runs and their statuses in the "Actions" tab of your GitHub repository.

### Authorizing Docker Hub Access

To enable GitHub Actions to push Docker images to Docker Hub, you need to set up two secrets in your repository:

- `DOCKERHUB_USERNAME`: Your Docker Hub username.
- `DOCKERHUB_TOKEN`: Your Docker Hub access token or password.

Follow these steps to add the secrets:

1. Go to the "Settings" tab of your GitHub repository.
2. Click on "Secrets" in the left sidebar.
3. Click on "New repository secret".
4. Enter `DOCKERHUB_USERNAME` as the name and your Docker Hub username as the value.
5. Click on "Add secret".
6. Repeat steps 3-5 for `DOCKERHUB_TOKEN`, using your Docker Hub access token or password as the value.

These secrets will be securely used by GitHub Actions to authenticate with Docker Hub during the Docker image push process.
