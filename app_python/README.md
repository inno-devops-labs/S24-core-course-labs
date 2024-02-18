## Overview

![CI badge](https://github.com/maintheme2/S24-devops-labs/actions/workflows/app_python.yml/badge.svg)

This app displays current Moscow time.

* Scalable
* Easy to use
* Absolutely useless :innocent:
* Flask-based

## Installation and running :fire:

* `git clone`
* `pip install -r requirements.txt`
* `python app.py`
* Go to the url specified in the command line.

## Docker :whale:

#### Build: (inside app_python folder)

* `docker build -t flask-msktime-app .`

#### Pull: 

* `docker pull maintheme/flask-msktime-app:v1`

#### Run:

* `docker run -p 5000:5000 -t maintheme/flask-msktime-app:v1`

## Testing :white_check_mark:

* `pip install pytest`

* Inside __app_python__ dir : `pytest`

## Continuous Integration :recycle:

The CI workflow ensures that every pull request has the code linted and tested before it can be merged. Additionally, it builds a Docker image of the application and pushes it to Docker Hub, ready for deployment. The use of GitHub secrets for sensitive information like Docker Hub credentials is a secure practice, as it prevents the credentials from being exposed in logs or the workflow file.