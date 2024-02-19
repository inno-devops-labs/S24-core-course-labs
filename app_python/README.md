# The Moscow Timezone python application

![Workflow Status](https://github.com/NikitaGrigorenko/DevOps/actions/workflows/main.yaml/badge.svg)

## Overview

The simple python application which display time in moscow time zone. Was built by using Flask framework.

## Installation instructions

Minimal Prerequisites:

- Python3
- pip packet manager
- Flask
- pytz library
- Docker

You can find the list of dependencies in requirements.txt file

## Environment Setup without Docker

```bash
# Navigate to the cloned Git repository folder with the source code of the tool
cd DevOps

# Navigate to the "app_python"
cd app_python

# Do not forget to run all commands in virtual environment
python3.11 -m venv env
source env/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Run application
python3 time_zone.app
# or 
python time_zone.app
```

### Sample Usage

To enter the application page just open in your browser

```bash
http://127.0.0.1:5000
```


## Environment Setup with Docker
For easier portability and deployment this app_python was been Dockerized. Its really simple to use docker package on the different platforms.

```bash
# Navigate to the cloned Git repository folder with the source code of the tool
cd DevOps

# Navigate to the "app_python"
cd app_python

# You can build your own docker image
docker build -t app_python . 

# Or pull existing one
docker pull nikitagrigorenko/app_python:latest

# Run docker image if you build your own:
docker run -p 5001:5000 app_python
# or if you pull existing one:
docker run -p 5001:5000 nikitagrigorenko/app_python:latest
```

### Sample Usage

After running a docker image open the following url in your browser:

```bash
http://127.0.0.1:5001
```

## Unit Tests

To test the application just run
```bash
python3 test_app.py
```

## CI workflow
- Checkout Code: The actions/checkout@v4 action checks out the repository code onto the runner, allowing subsequent steps to access the code.

- Set Up Python: The actions/setup-python@v2 action sets up a specific version of Python on the runner. In this case, Python 3.11 is used.

- Cache Dependencies: The actions/cache@v2 action caches the pip cache directory to speed up future installations of dependencies.

- Install Dependencies: The dependencies listed in app_python/requirements.txt are installed using pip. The python -m pip install --upgrade pip command ensures that pip itself is up to date.

- Run Tests: The test_app.py script is executed to run tests on the application.

- Security Check: The snyk/actions/python-3.10@master action runs a security check on the Python dependencies in the app_python/ directory.

- Linting: The py-actions/flake8@v2 action runs flake8 to lint the Python code and check for style issues.

- Set Up Docker Buildx: The docker/setup-buildx-action@v1 action sets up Docker Buildx, which is a CLI plugin that extends the docker command with the full support of the features provided by Moby BuildKit builder toolkit.

- Cache Docker Layers: The actions/cache@v2 action caches Docker layers to speed up subsequent Docker builds.

- Log in to Docker Hub: The docker/login-action@v1 action logs in to Docker Hub using the provided credentials, stored securely as GitHub Secrets.

- Build and Push Docker Image: The docker/build-push-action@v2 action builds a Docker image from the Dockerfile in the app_python directory and pushes it to Docker Hub if the workflow was triggered by a tag.


## File Structure

- `PYTHON.md`: Contains the breif explanation of best practicies while using Flask.
- `requirenments.txt`: Contains all dependencies.
- `time_zone.py`: Contains python code with Flask server and timezone of Moscow getting.
- `DOCKER.md`: Contains the breif explanation of best practicies while using Docker
- `Dockerfile`: Contains all the commands a user could call on the command line to assemble an image.
