![Status badge](https://github.com/timur-harin/S24-core-course-labs/.github/workflows/python.yml/badge.svg)


# Lab1 flask web app

Application to get moscow time

## Prerequisites

Ensure you have [Python](https://www.python.org/) installed on your system. This
project uses [Poetry](https://python-poetry.org/) for dependency management.


## How to build

```bash
docker build -t timur_devops .
```

## How to pull

```bash
docker pull timur_harin_devops:latest 
```

## How to run

```bash
docker run --name app -d -p 8080:5000 timur_harin_devops:latest
```

## Use

Service is here `http://127.0.0.1:8080`

<br> <br/>

## Installation (legasy)

Clone the repository and navigate to the project directory. Install the
dependencies using Poetry:

```bash
poetry install
```

## Running the Application

Start the application using the following command:

```bash
poetry run python app.py                 
```

Upon successful startup, you should see output similar to this:

```bash
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

You can now access the service by visiting `http://127.0.0.1:5000`. For example:

```bash
$ curl http://127.0.0.1:5000
The current time in Moscow: 08:47:07
```

## Testing

This project uses [pytest](https://docs.pytest.org/en/7.4.x/) for testing. It's
important to update and run tests to ensure the application's reliability. Run
the tests using the following command:

```bash
poetry run pytest
```

## CI

### Triggers and Jobs Summary

#### Triggers:
Triggers are events that initiate a workflow run. In the provided YAML configuration, the triggers specified are:
- **push:** Triggers the workflow when code is pushed to the main branch.
- **pull_request:** Triggers the workflow when a pull request is opened or updated on the main branch.

#### Jobs:
Jobs are a collection of steps that execute on the same runner. In the YAML configuration, there are two jobs defined:
1. **install_clear_test_lint:**
   - **Runs on:** ubuntu-latest
   - **Steps:** Includes setting up Python, caching dependencies, installing Poetry, installing dependencies, running tests, and running linting.

2. **docker:**
   - **Runs on:** ubuntu-latest
   - **Steps:** Includes logging in to Docker Hub, building a Docker image, and pushing the image to Docker Hub.

Jobs in a workflow can run in parallel or sequentially, depending on the configuration. Each job can have its own specific runner and steps.