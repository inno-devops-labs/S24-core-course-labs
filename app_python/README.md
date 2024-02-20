# Python Web Application: Moscow Time

## Overview

This is a Python web application built with Flask to display the current time in Moscow.

## Features

- Displays the current time in Moscow.
- Automatic updating of time upon page refreshing.

## Project Structure

- `app.py`: Main application logic.
- `templates`: HTML templates.
- `static`: Static files (CSS).
- `PYTHON.md`: Documentation about the project and development details.
- `README.md`: Project overview and instructions.

## Getting Started

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2. Run the application:

   ```bash
   python app.py

3. Open your web browser and navigate to `http://127.0.0.1:5000/` to view the application.

## Docker

- The containerized application uses a minimal Python 3.8-slim base image and follows Docker best practices. The
  application is configured to run as a non-root user, and it exposes port 5000. The necessary dependencies are
  installed, and the application files are copied into the container. The entry point is set to run the app.py Python
  script.

### Docker Instructions:

1. Build Docker Image:

    - Run the following command to build the Docker image:

    ```bash
   docker build -t devops-lab app_python

2. Run Docker Container:

    - To run the Docker container, execute the following command:

   ```bash
   docker run -p 5000:5000 devops-lab

3. Pull Docker Image (Optional)

    - To pull the image instead of building locally, run:

   ```bash
   docker pull exemplerie/devops-lab

4. Access the Application:

    - Once the container is running, open a web browser and navigate to http://localhost:5000 to access the application.

## Unit tests

- The project includes unit tests to ensure the correctness of specific functions and features. To run the unit tests, you can use the following command:

   ```bash
   pytest

- The project includes comprehensive unit tests to ensure the correctness and reliability of specific functions and features. These tests cover various aspects of the application, including:

   - Time Handling: Ensuring the accurate conversion of time zones and correct display of the Moscow time.

   - HTML Template Rendering: Verifying that the HTML templates are correctly rendered and contain the expected content.



