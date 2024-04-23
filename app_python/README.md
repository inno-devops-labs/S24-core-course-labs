[![CI](https://github.com/Tyu-cr/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)](https://github.com/Tyu-cr/S24-core-course-labs/actions/workflows/main.yaml)

## Overview

This simple Python web application is built using the FastAPI framework to display the current time and date in Moscow.
For now you have to refresh the browser page manually to update the time.

## Dependencies

**FastAPI:** FastAPI is used as the web framework for building the API endpoints.  
**Pytz:** Pytz is used for working with timezones and getting the current time in Moscow.  
**Uvicorn:** Uvicorn is used as the ASGI server to run the FastAPI application.

## How to run

1. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Run `main.py` from the `app_python` directory of a project to start the FastAPI server:
    ```bash
    python .\main.py
    ```
3. Open a web browser and go to `http://localhost:8000`

## Template

A small `index.html` template is used to better visualize the current time in Moscow in the browser.

## Visits

Application also track number of times it was accessed and store it in file `visits.txt`

It can be shown at http://localhost:8000/visits

## Docker

### How to build

To build the Docker image, move to the app_python directory:

```bash
cd .\app_python\
```

and execute the following command to create a docker image:

```bash
docker build -t monykekker/my_app .
```

### How to pull?

You can pull already existing image using this command:

```bash
docker pull monykekker/my_app:latest
```

### How to run?

To run the Docker container, execute the following command:

```bash
docker run -p 8000:8000 monykekker/my_app
```

Then go to the [localhost:8000](http://localhost:8000/) to see Moscow time.

## Unit Tests

To run the tests:

- Run the following command in `app_python` directory of a project:

   ```bash
   pytest .\tests\test.py
   ```

## Continuous Integration Workflow

These are the core steps for CI workflow:

1. **_Dependencies_**: Install project dependencies specified in the `requirements.txt`.
2. **_Linter_**: Check code style using a `flake8`.
3. **_Tests_**: Run unit tests using `pytest`.
4. **_Vulnerability checks_**
    - Use Snyk for Vulnerability checks.
5. **_Docker Integration_**:
    - **_Login_**: Authenticate with Docker Hub.
    - **_Build and Push_**: Build the Docker image and push it to Docker Hub.