# Project Name: Time Display Web Application

## Description

This web application displays the current time in Moscow. It is built with Flask, a lightweight WSGI web application framework in Python. The application demonstrates the use of Flask for creating web applications, handling routes, rendering templates, and displaying dynamic content based on the server's timezone.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Tests](#tests)
- [Best Practices](#best-practices)
- [License](#license)

## Installation

Follow these steps to set up your development environment:

1. **Clone the repository**

```
git clone https://github.com/tanmaysharma2001/S24-core-course-labs.git
```

Switch branch to 'lab 01'.

2. **Set up a virtual environment**

Navigate to the project directory.

Create a virtual environment:

```
python -m venv venv
```


Activate the virtual environment:

- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

3. **Install dependencies**

```
pip install -r requirements.txt
```


## Usage

To run the application locally:

1. **Start the Flask application**

```
python run.py
```


2. **Visit the application**

Open a web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Tests

To run tests, execute the following command:

```
python test_app.py
```

Ensure all tests pass before submitting a pull request for your changes.

## Best Practices

This project adheres to the following best practices:

- **Code Style**: Follows PEP 8 style guide for Python code.
- **Security**: Implements input validation and output encoding to protect against common vulnerabilities.
- **Testing**: Includes comprehensive unit tests to ensure functionality and prevent regressions.

For more details, refer to the [PYTHON.md](PYTHON.md) document.

## Docker

The Time Display Web Application is also containerized using Docker, allowing for easy setup, deployment, and distribution. Below are the instructions for building, pulling, and running the Docker container.

### How to Build

To build the Docker image for the application, follow these steps:

1. **Navigate to the project directory** where the `Dockerfile` is located.

2. **Build the Docker image** using the following command:

```bash
docker build -t time-display-app .
```
Replace time-display-app with your preferred image name.

### How to Pull

The Docker image is available in a registry, you can pull it directly instead of building it locally:
```bash
docker pull sharmatanmay617/devops-lab-2
```

### How to Run

To run the application inside a Docker container, use the following command:

```bash
docker run -p 5000:5000 sharmatanmay617/devops-lab-2
```
This command runs the Docker container and maps port 5000 of the container to port 5000 on your host machine, allowing you to access the application through your browser.

### Accessing the Application

After starting the container, open a web browser and navigate to http://127.0.0.1:5000/ to view the application.