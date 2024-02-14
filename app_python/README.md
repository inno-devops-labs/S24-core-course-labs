# Flask Web Application 

## Overview

This is a flask web application that renders current time in Moscow zone. 

## Steps to run the application 

1. Install `Python 3`.

2. Navigate to `app_python` directory.

3. Set up virtual environment.
    - On Windows: `python -m venv venv`.
    - On Unix-based systems: `python3 -m venv venv`.

4. Activate the virtual environment.
    - On Windows: `.\venv\Scripts\activate`.
    - On Unix-based systems: `source venv/bin/activate`.

4. install requirements `pip install -r requirements.txt`.

5. Run `flask --app flaskr/app run`.

## Steps to test the application 
 
1. Navigate to `app_python` directory.

2. Set up virtual environment, activate it and install requirements as mentioned previously.

3. Run `pytest`.

## Steps to build docker  

1. navigate to `app_python` directory. 

2. run `docker build -t name .`

## Steps to run docker  

- run `docker run -p 5000:5000 name`

## Steps to push docker image

1. `docker login`
2. `docker tag name yourusername/name`
3. `docker push yourusername/name`

## Steps to pull and run docker image
1. `docker pull yourusername/name`
2. `docker run -p 5000:5000 yourusername/name`

