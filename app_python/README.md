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
  - From Dockerhub: `docker pull ieorekhov/s24-devops:lab2`
  - Build from Dockerfile: `docker image build -t ieorekhov/s24-devops:lab2 .`
- `docker run -d -p 5000:5000 ieorekhov/s24-devops:lab2`
- Open `http://localhost:5000/` in a browser.

