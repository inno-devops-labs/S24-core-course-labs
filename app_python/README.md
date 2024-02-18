[![Python App CI](https://github.com/NAD777/S24-DevOps/actions/workflows/app_python.yaml/badge.svg)](https://github.com/NAD777/S24-DevOps/actions/workflows/app_python.yaml)

# Simple Flask app
The idea of the app is really simple, it just shows the current time in Moscow

# Set up
1. Firstly it is preferable to use virtual environment for `python`:
```bash
python3 -m venv env
```
2. Activate the virtual environment
```bash
source env/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python app.py
```
- Directly (using python)
```bash
python app.py
```
- Using docker image (see below)

# Unit Tests and others
All tests can be found in the directory `tests`, to run them use the following command:
```bash
pytest tests/*.py
```

# Stack
- Python
- Flask
- Pytests
- BeautifulSoup (for tests)
- Requests (for tests)
– Logging (standard library)

# Docker
## Build
To build docker image you can use the following command:
```bash
docker build -t {docker_image_name} .
```
for example:
```bash
docker build -t anton_flask .
```

## Pull
To pull this image from Docker hub [link](https://hub.docker.com/repository/docker/nad777/anton_nekhaev_flask/general). You can use the following command:
```bash
docker pull nad777/anton_nekhaev_flask:latest
```
## Run
To run you docker image after build you need to use the following command:
```bash
docker run -p 5001:5001 {docker_image_name}
```
for example:
```bash
docker run -p 5001:5001 anton_flask
```
**OR** (if you pull from Docker hub)
```bash
docker run -p 5001:5001 nad777/anton_nekhaev_flask:latest
```

# Python App CI

This repository is configured with Continuous Integration (CI) practices via GitHub Actions. All updates to the codebase (push and pull events) trigger the CI workflow as specified in .github/workflows/main.yml. The workflow is set to respond to pushes and pull requests that affect the files in the .github/workflows/ or app_python/ directories.

The CI workflow involves the following jobs:

1. build-and-test: This job sets up the environment on the latest Ubuntu, installs Python along with the relevant dependencies, lints the codebase with flake8, and runs pytest for all unit tests. Dependencies are cached to speed up the process. 

2. security: This checks for vulnerabilities in the Python version. It uses Snyk and requires an API token. 

3. docker: This job logs in to Docker, builds and pushes a Docker image only if the preceding jobs succeed. 

The Docker build and push action is run only when build-and-test and security jobs complete successfully. This ensures that the Docker image is only built and pushed when the codebase passes all checks, tests, and vulnerability scans.