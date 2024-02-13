# Python Web Application: Moscow Time Display

## Overview

This Python web application displays the current time in Moscow. It utilizes the Flask framework to create a lightweight web server at `http://127.0.0.1:5000/` and returns the current time in JSON format.

## Local Installation

Follow these steps to set up the application locally:

1. Clone this repository:

    ```bash
    git clone <repository_url>
    cd app_python
    ```

2. Install dependencies using pip and virtual environment:

    ```bash
        For linux:
        python -m venv venv && source venv/bin/activate
        For windows in GitBash:
        python -m venv venv && source venv/Scripts/activate
        pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Requirements

- Python 3.x
- Flask
- pytz
- freezegun

## Structure

- `app.py`: Contains the application logic.
- `requirements.txt`: Lists the dependencies required to run the application.
- `test_app.py`: Contains unit tests for the application.
- `PYTHON.md`: Describes best practices, coding standards, and testing approaches applied.
- `README.md`: Overview of the application.
- `.flake8`: Config for flake8 linter to run flake8 for whole project

## Docker

The application has been containerized using Docker. Follow the steps below to build, pull, and run the containerized application.

### How to build?

To build the Docker image, run the following command:
```docker build -t my_app .```


### How to pull?

To pull the pre-built Docker image from the Docker Hub, run the following command:
```docker pull levgo/devopslab```


### How to run?

To run the containerized application, execute the following command:
```docker run -p 5000:5000 my_app```


After running the above command, you can access the application at http://localhost:5000.