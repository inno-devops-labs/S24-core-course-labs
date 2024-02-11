## Overview

This app displays current Moscow time.

* Scalable
* Easy to use
* Absolutely useless :innocent:
* Flask-based

## Installation and running :fire:

* git clone
* pip install -r requirements.txt
* python app.py
* Go to the url specified in the command line.

## Docker :whale:

#### Build: (inside app_python folder)

* `docker build -t flask-msktime-app .`

#### Pull: 

* `docker pull maintheme/flask-msktime-app:v1`

#### Run:

* `docker run -p 5000:5000 -t maintheme/flask-msktime-app:v1`