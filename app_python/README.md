# "Time in Moscow" Web Application

## Overview

This Python web application displays the current time in Moscow.

Open the index page at `/` and web server built with Python will generate a static HTML web page with the current time in Moscow.

## Features

- 🕰️ Displays current time in Moscow;
- 💨 Fast, <3kb plain HTML;
- 💪🏻 Robust, built with [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Local Setup

_Step 0_. This application uses [type hints](https://docs.python.org/3/library/typing.html) and Flask, therefore, **Python 3.8** or newer is required.

_Step 1_. Open the `app_python` directory and run commands below from there.

_Step 2_. Create and activate virtual environment:

```sh
# Create
python -m venv venv

# Activate in bash and other shells
source ./venv/bin/activate

# Activate in fish
source ./venv/bin/activate.fish
```

_Step 3_. Install requirements:

```sh
pip install -r requirements.txt
```

_Step 4_. Run web-application:

```sh
python -m flask --app app/main:app run --port=8000
```

_Step 5_. Go to [localhost:8000](http://localhost:8000) in the browser, you should see the current time in Moscow.

## Docker

### Building image

To build image, use the following command (substitute `x.y.z` with the actual version):

```sh
docker build -t devops-simple-app:x.y.z .
```

### Pulling image from Docker Hub

Docker image is available on Docker Hub, to pull it use the following command:

```sh
docker pull evermake/devops-simple-app:latest
```

### Running container

To run the container, use the following command:

```sh
docker run -p 8000:8000 evermake/devops-simple-app
```

App will be available at [localhost:8000](http://localhost:8000).
