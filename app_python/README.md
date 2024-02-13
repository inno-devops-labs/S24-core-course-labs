# Moscow Time Zone Application

## Overview
This application is a simple Python application that returns the current time in Moscow. 

## Features
- Displays the current time in Moscow

## Local installation details

To use this application, simply run the following commands:

```bash
# Make sure you are in the app_python directory
cd app_python

# Check if you have Python installed
python --version

# Install the dependencies
pip install -r requirements.txt

# Run the application
flask run

# For debug mode: 
flask run --debug
```

Open your browser and navigate to http://localhost:5000/ to see the current time in Moscow.

## Docker
This application is also available as a Docker container. To run the application in a Docker container, follow the instructions below.

- **Build locally**
  ```bash
    # Make sure you are in the app_python directory
    pwd

    # Build the Docker image
    docker build --tag abuwho/app_python:latest .

    # Run the Docker container
    docker run -d -p 5000:5000 abuwho/app_python:latest
  ```
  Open your browser and navigate to http://localhost:5000/

Or, 

- Pull from Docker Hub
  ```bash
    # Pull the Docker image
    docker pull abuwho/app_python:latest

    # Run the Docker container
    docker run -d -p 5000:5000 abuwho/app_python:latest
  ```
  Open your browser and navigate to http://localhost:5000/