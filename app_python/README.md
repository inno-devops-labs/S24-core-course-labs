![app_python](https://github.com/ananastya1/S24-core-course-labs/workflows/Main%20CI/badge.svg)


# Python Web Application - Moscow Time Display

## Overview
This Python web application is designed to display the current time in Moscow. It's built with the Flask framework, offering a simple interface that refreshes to update the time displayed.

## Features

- Displays the current Moscow time in a simple web interface.
- Time updates on page refresh.

## Prerequisites
Before running this application, ensure you have the following installed:

- Python 3.x
- Flask
- pytz (for timezone handling)

## Installation
Clone the repository to your local machine:

```
git clone https://github.com/ananastya1/S24-core-course-labs
cd app_python
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the Application
To run the application, execute:

```
python app.py
```
Navigate to http://127.0.0.1:5000/ in your web browser to view the application.

## Testing
### Unit Testing
Ensure all tests pass by running:

```
pytest
```

### Test Coverage
For test coverage, run:

```
coverage run -m unittest discover
coverage report
```

## Docker

The application is containerized using Docker, allowing for easy deployment and scaling. 
Below are instructions on how to interact with the Dockerized application.

To build the Docker image:
```
docker build -t ananastya10/devops:lab2 . 
```

To pull the Docker image:

```
docker pull  ananastya10/devops:lab2   
```

To run the Docker container:
```
docker run -d -p 5000:5000 -t ananastya10/devops:lab2  
```

## CI

The CI file is located at .github/worflows/main.yaml

CI consists of:

- Python Setup
- Dependencies Installation
- Linter 
- Testing
- Login to Docker Hub
- Build and Push to Docker Hub
