# Python Web Application
[![lint-test-security-check](https://github.com/Darverda/DevOps_labs/actions/workflows/main.yaml/badge.svg)](https://github.com/Darverda/DevOps_labs/actions/workflows/main.yaml)

This is a Python web application that displays the current time in Moscow.

## Overview

The Python web application uses the Flask framework to create a simple web page that shows the current time in Moscow. It consists of a single route that renders an HTML template to display the time.

## Installation

1. Clone the repository:
```git clone <https://github.com/Darverda/DevOps_labs>```

2. Install the required dependencies:
```pip install -r requirements.txt```

## Usage

1. Run the application:
```python app.py```

2. Open a web browser and navigate to `http://localhost:5000` to see the current time in Moscow.

### License

This project is licensed under the [MIT License](LICENSE).

## Using Docker

This application can be containerized using Docker. Follow the instructions below to build, pull, and run the Docker image.

### Requirements

- Rootless container environment
- Docker installed

### Build

To build the Docker image, navigate to the project directory and run the following command:
```docker build -t darverda/app . ```

### Pull
If you prefer to pull the pre-built Docker image from a registry, you can use the following command:
```docker pull darverda/app:latest ```

### Run
To run the Docker container, use the following command:
```docker run -p 5000:5000 --name app darverda/app:latest```

## CI Workflow
The CI workflow is set up using GitHub Actions. There are three workflows: **Lint**, **Test** and **shyk**
### Lint Workflow

The Lint workflow checks the code for any linting issues using `pylint`.

The workflow is triggered on every push & pull request in the repository.