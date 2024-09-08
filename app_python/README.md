
![Python application](https://github.com/KatyKoshmanova/S24-core-course-labs/workflows/python-app.yml/badge.svg)

# Python Web Application

## Overview:

This Python web application displays the current time in Moscow. It utilizes the Flask micro-framework for simplicity and flexibility.

## Requirements:

- Python 3.5+
- Flask

## Installation:

1. Clone the repository:

   ```bash
   git clone <repository_url>
    ```
2. Navigate to the `app_python` directory:

   ```bash
   cd app_python
   ```
3. Install the required packages:

   ```bash
    pip install -r requirements.txt
    ```
4. Run the application:

   ```bash
   python app.py
   ```
5. Open a web browser and go to `http://http://127.0.0.1:5000/` to view the application.

# Docker

Our application is containerized using Docker, which ensures it can run consistently on any platform that supports Docker.

## Building the Docker Image

1. To build the Docker image, navigate to the `app_python` directory and run the following command:

```bash
docker build -t image:latest .
```

2. To pull the image from Docker Hub, run the following command:

```bash
docker pull katykoshmanova/image:latest
```

3. To run the Docker container, use the following command:

```bash 
docker run -p 5000:5000 katykoshmanova/image:latest
```

## Unit Tests

In the `unittest1.py` file, two unit tests have been created for the web application.

- The first test, `test_display_time`, verifies the application's root URL returns a 200 status code, indicating a successful HTTP request, and that the response data contains the string 'Current Time in Moscow'. This ensures the application is correctly displaying the time.

- The second test, `test_time_format`, validates the time displayed on the application's root URL matches the format YYYY-MM-DD HH:MM:SS, ensuring the application is correctly formatting the time.

These tests are written following best practices such as:

- **Modularity:** Each test is a separate method within the `TestApp` class, allowing each test to be run independently.

- **Setup and Teardown:** The `setUp` method is used to initialize the test client before each test, ensuring a clean state.

- **Assertion Methods:** The `unittest` framework's assertion methods are used to check for expected outcomes, providing clear error messages when tests fail.

- **Test Naming:** Test methods are named in a way that describes their function, improving readability and maintainability.

- **Regular Expressions:** Regular expressions are used to match the time format, providing a flexible and precise way to validate the output.

To run the unit tests, use the following command:

   ```bash
   python -m unittest unittest1.py
   ```


## Continuous Integration (CI)

This project uses GitHub Actions for Continuous Integration. The CI workflow includes the following steps:

1. **Set up Python:** The workflow sets up a Python environment with the specified version (3.8 in this case).

2. **Install dependencies:** The workflow installs the necessary dependencies for the project using pip. It also upgrades pip to the latest version.

3. **Lint with flake8:** The workflow uses flake8, a Python linting tool, to check the code for potential errors.

4. **Test with pytest:** The workflow runs unit tests using pytest to ensure the code behaves as expected.

5. **Login to DockerHub:** The workflow logs into DockerHub using the provided username and password.

6. **Build and push Docker image:** The workflow builds a Docker image of the application and pushes it to DockerHub.

To see the results of the CI workflow, check the "Actions" tab in the GitHub repository.