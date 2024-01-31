# "Time in Moscow" Web Application

## Overview

This Python web application displays the current time in Moscow.

Open the index page at `/` and web server built with Python will generate a static HTML web page with the current time in Moscow.

## Features

- 🕰️ Displays current time in Moscow;
- 💨 Fast, <3kb plain HTML;
- 💪🏻 Robust, built with [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Local Setup

0. This application uses [type hints](https://docs.python.org/3/library/typing.html) and Flask, therefore, **Python 3.8** or newer is required.

1. Open the `app_python` directory and run commands below from there.

2. Create and activate virtual environment:

```sh
# Create
python -m venv venv

# Activate in bash and other shells
source ./venv/bin/activate

# Activate in fish
source ./venv/bin/activate.fish
```

3. Install requirements:

```sh
pip install -r requirements.txt
```

4. Run web-application:

```sh
python -m flask --app app/main:app run --port=8000
```

5. Go to http://localhost:8000 in the browser, you should see the current time in Moscow.
