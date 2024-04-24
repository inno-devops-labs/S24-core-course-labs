# My Python Web Application
[![app python](https://github.com/a1kuat/S24-core-course-labs/actions/workflows/main.yml/badge.svg?branch=lab3)](https://github.com/a1kuat/S24-core-course-labs/actions/workflows/main.yml)

## Overview
This application displays the current time in Moscow using the Flask framework.
## Features
- Displays the current time in Moscow.
- Automatically updates the time upon page refresh.

## Installation
1. Clone the repository: `git clone https://github.com/a1kuat/S24-core-course-labs.git`
2. Change into the project directory: `cd app_python`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python app.py`

## Usage
Navigate to `http://localhost:5000` in your web browser to view the current time in Moscow.

## Building the Docker Image

To build the Docker image, navigate to the directory containing the `Dockerfile` and run:

`bash docker build -t my-python-app . `


## Pulling the Docker Image

The image is pushed to my Docker Hub, you can pull it using:

`bash docker pull a1kuat/my-python-app`

## Running the Docker Image

To run the Docker image locally, use:

`bash docker run -p 5000:5000 my-python-app`


Then visit `http://localhost:5000` in your web browser to see the application in action.

## Unit Tests

We've written unit tests for our Flask application using `pytest`. These tests ensure that the application behaves as expected.

To run the unit tests locally, use the following command:

`bash pip install pytest pytest app_python/test_app.py`

## Continuous Integration

We've set up a CI workflow using GitHub Actions to automatically build and test our Python project whenever changes are pushed to the main branch or a pull request is opened.

The CI workflow includes the following steps:

- Checkout the code
- Set up Python  3.8
- Install dependencies
- Lint the code with flake8
- Run unit tests with pytest
- Build and push a Docker image

You can view the status of the CI workflow by clicking on the "Actions" tab at the top of this repository.

## New Features

- **Visit Counter**: The application now keeps track of the number of visits. Each visit increments a counter stored in a file named `visits`.
- **Visits Endpoint**: A new endpoint `/visits` has been introduced to display the total number of visits recorded so far.

## Testing the Visit Counter

1. Start the application using `docker-compose up`.
2. Open a web browser and navigate to `http://localhost:5000/visits` to view the current visit count.
3. Refresh the page to increment the visit count and observe the change reflected in real-time.