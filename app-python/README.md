
![CI](https://github.com/FurryLord/DevOps24/workflows/CI/badge.svg)


## Overview of project

### 1. Purpose

This simple [Python app](/app_python/)  used to display current Moscow (UTC-3) time.

### 2. Stack
- Framework: ``flask``
- Templates of pages: ``Django HTML``
- Time calculation: ``datetime`` library
- Testing: ``unittest`` library
- Logging: ``logging`` library


### 3. Structure

- ``app.py`` performs routing at ``/`` and calculates Moscow time.
- ``test_app.py`` performs unit test to validate the correctness of time.
- ``app.log`` contains logs of application during its work.

#### 3.1. Tempelates
-  ``index.html`` is the main page where time is shown.
-  ``error.html`` contains a message that error has occured.

#### 3.2. Documentation
- ``PYTHON.md`` describes the reasons of choosing ``flask`` and best practices applied to the project.
- ``README.md`` describes the overall structure of project.


### 4. Get started
- Run ``pip install -r requirements.txt``.
- Run `` python  app.py`` inside ``app_python`` folder.
- Go to ``http://127.0.0.1:5000/``.
- You can check number of visits on ``http://127.0.0.1:5000/visits``

### 5. Docker

#### 5.1. Containerization process

This Dockerfile containerizes a Python Flask application, ensuring security, efficiency, and ease of deployment. 

It utilizes a specific version of the Python slim image (Python 3.9) to minimize the image size. A non-root user, `appuser`, is created to run the application, enhancing security by limiting privileges. The application files (`requirements.txt`, `app.py`) are copied into the `/app` directory, along with the templates for the Flask application. Dependencies are installed using `pip`, and port 5000 is exposed to allow external access to the Flask application.

A data directory is also created to store any necessary data files.

Additionally, a logging directory is created within the container to store application logs. Finally, the Flask application (`app.py`) is set to run automatically when the container launches. 
#### 5.2. How to build?
`docker build -t lab2 .`
#### 5.3.  How to pull?
`docker pull furryowolord/lab2`
#### 5.4. How to run?
`cd .\app_python\`
`docker run -p 5000:5000 furryowolord/lab2`

### 6. Unit tests

 These tests cover different aspects of the Flask application, including calculation logic, template rendering, and error handling, ensuring that the application functions correctly under various conditions:

1. **test_moscow_time_calculation**: This test ensures that the displayed time on the homepage (`/`) is correctly calculated as the current UTC time plus 3 hours, which corresponds to Moscow time. It compares the expected Moscow time string with the actual displayed time string on the webpage.

2. **test_template_rendering**: This test checks that the homepage (`/`) renders the correct template, which includes the text "Current time in Moscow:".

3. **test_error_route**: This test checks that the error route (`/error`) returns a status code of 200 (OK) and includes the expected error message "An error occurred" in the response data.

### 7. CI Pipeline

This repository uses GitHub Actions to automate the build, test, and Docker image deployment process. The CI pipeline consists of the following steps:

1. **Dependencies**
   - Check out the code from the repository.
   - Set up Python environment using the specified version.
   - Install project dependencies listed in the `requirements.txt` file.

2. **Linter**
   - Use Flake8 to lint the Python code for style and formatting errors.

3. **Tests**
   - Run unit tests using the `unittest` framework to ensure code functionality.

4. **Docker Integration**
   - Login to Docker Hub using the provided credentials stored as GitHub Secrets.
   - Build a Docker image tagged as `yourusername/yourimage:latest`.
   - Push the Docker image to Docker Hub for deployment.

The CI pipeline is triggered on each push to the `main` branch, ensuring that changes are automatically tested and deployed to Docker Hub when the code is merged.
