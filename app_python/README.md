# Python Web Application Documentation
[![CI](https://github.com/anastasia-martynova/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)](https://github.com/anastasia-martynova/S24-core-course-labs/actions/workflows/main.yaml)

## Description
This Python web application displays the current time in Moscow. It was developed using Flask framework, following best practices and coding standards.

## Features
- Displays the current time in Moscow.

## Framework Used
- Framework: Flask
- Justification: Flask was chosen for its simplicity, flexibility, Pythonic nature, and suitability for smaller web projects.


## Installation and running locally
1. Clone the repository:
 ```bash
   git clone <repository-url>
 ```
2. Install dependencies:
 ```bash
   pip install -r requirements.txt
 ```
3. Run the application:
```bash
    python app.py
 ```

## Docker
This application is containerized using Docker for easy deployment and portability.
### Instructions for execution

1. Building the Image:
   ```bash
   docker build -t my-app .
   ```

2. Pulling the Image (Optional if not built locally):
   ```bash
   docker pull anastasiamartynova/my-docker-repo:latest
   ```

3. Running the Container:
   ```bash
   docker run -p 8080:8080 anastasiamartynova/my-docker-repo:latest
   ```


## File Structure

- `app.py`: Main Flask application file.
- `requirements.txt`: Python packages with their versions necessary for running the application.
- `PYTHON.md`: Explains Flask choice; covers coding standards & testing.

## Unit Tests
Unit tests cover essential functionalities, such as displaying the current time in Moscow, and verify the expected behavior of the application.

### Running Unit Tests:
To run the unit tests:
```bash
python -m unittest test.py
```

## Continuous Integration (CI) Workflow
### Workflow Steps:
1. Dependencies Installation: Installs project dependencies specified in requirements.txt.
2. Linting: Runs pylint to ensure code quality and adherence to Python best practices.
3. Unit Tests: Executes unit tests to verify the functionality of the Python code.
4. Docker Image Building and Pushing:
   - Login to Docker Hub: Authenticates with Docker Hub using GitHub Actions.
   - Build and Push Docker Image: Builds a Docker image and pushes it to the Docker Hub registry for deployment.

### How to Run the CI Workflow:
1. When a push event occurs in the repository, the CI workflow is automatically triggered.
2. The workflow can be found in the .github/workflows/main.yaml file.
