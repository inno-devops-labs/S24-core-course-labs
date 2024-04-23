# Python Web Application

## Overview
This is a simple Python web application that displays the current time in Moscow. It utilizes the Flask framework for web development and pytz library for time zone conversion.
This web application also count number of visits. You can access to number of visits through adding ```/visits```.

## Installation
1. Clone the repository:
>git clone https://github.com/Snapman7/S24-devOps
2. Navigate to the `app_python` directory:
>cd app_python
3. Install dependencies:
>pip install -r requirements.txt

## Usage
1. Run the application:
>python3 time_web.py
2. Follow the instructions in terminal.

## Docker Containerization

This section explains how to containerize and run the application using Docker.

### Build

To build the Docker image:

```bash
docker build -t time_web.py .
```

Ensure you are in the directory containing the Dockerfile.

### Pull

To pull the Docker image from Docker Hub:

```bash
docker pull snapman/time_web
```

### Run

To run the Docker container:

```bash
docker run -p 5000:5000 snapman/time_web
```

Make sure to meet the following requirements:

- Use a rootless container
- Utilize COPY for specific files only
- Ensure layer sanity
- Use a precise version of the base image and language (e.g., python:3-alpine3.15)
```
