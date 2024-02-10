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

### 5. Docker

#### 5.1. Containerization process

This Dockerfile containerizes a Python Flask application, ensuring security, efficiency, and ease of deployment. 

It utilizes a specific version of the Python slim image (Python 3.9) to minimize the image size. A non-root user, `appuser`, is created to run the application, enhancing security by limiting privileges. The application files (`requirements.txt`, `app.py`) are copied into the `/app` directory, along with the templates for the Flask application. Dependencies are installed using `pip`, and port 5000 is exposed to allow external access to the Flask application. 

Additionally, a logging directory is created within the container to store application logs. Finally, the Flask application (`app.py`) is set to run automatically when the container launches. 
#### 5.2. How to build?
`docker build -t lab2 .`
#### 5.3.  How to pull?
`docker pull furryowolord/lab2`
#### 5.4. How to run?
`cd .\app_python\`
`docker run -p 5000:5000 furryowolord/lab2`

          