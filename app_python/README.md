# Overview

A simple web application written in Python that displays Moscow time, enjoy!

## Installation guide

- Python 3.10+
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python ./app.py`
- Open `http://localhost:5000/` in a browser.

## Docker installation guide

- You can prefer running an application via Docker rather than installing packages locally.
- Obtain an image, you have two options:
  - From Dockerhub: `docker pull ieorekhov/s24-devops:lab3`
  - Build from Dockerfile: `docker image build -t ieorekhov/s24-devops:lab3 .`
- `docker run -d -p 5000:5000 ieorekhov/s24-devops:lab3`
- Open `http://localhost:5000/` in a browser.


## Unit tests
- Unit tests were written to ensure code quality and reliability.
  - Test **test_status_code** verifies that the base route returns a correct status code 200.
  - Test **test_time** verifies that the displayed time on the base page returns correct Moscow time. It compares the expected Moscow time with an actual output on the page.

## CI workflow
![CI workflow](https://github.com/elintendo/S24-core-course-labs/actions/workflows/main.yml/badge.svg)
- Workflow triggers when push to lab3 or main branch takes place.
- Python build cache was utilized to enhance workflow efficiency.
- Snyk checks are implemented in workflow file.
- Linting, testing, docker deploying work properly.

## Counter
The application now keeps track of the number of times it's accessed using a counter. A new endpoint `/visits` has been introduced to display the recorded number of visits.
