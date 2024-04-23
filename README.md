# Moscow Timezone

## Name

Rostislav Zhukov

## Description

This project is an app that shows current time in Moscow timezone.

For every reload, it updates time.

## Installation

In order to run project, you need `python` of version 3 and higher, `pip`.

Then, git clone repo, checkout to lab1. Go to app_python directory.

Create new virtual environment:

```bash
python3 -m venv env
```

For Windows:
```bash
py -m venv env
```

Activate virtual ENV:

```bash
source env/bin/activate
```

For Windows:
```bash
path\to\env\Scripts\activate.bat
```

Install necessary modules:

```bash
pip install -r requirements.txt
```

For Windows:
```bash
py -m pip install -r requirements.txt
```

## Usage

Run application:

```bash
flask run
```

For Windows:
```bash
py -m flask run
```

By default, it will run on localhost:5000.

Such behavior can be changed with `port` and `host` command-line options.

Then, in browser go to `127.0.0.1:5000` or any other custom configuration {HOST}:{PORT}

##Docker

To build I used such command:

```bash
docker build -t hallejujah/devops_app .
```

There is another way of running the application which requires Docker installed.

Once you have it installed, run:

```bash
docker pull hallejujah/devops_app
```

Command above will pull an image from Docker Hub. Run a container from it:

```bash
docker run -p 5000:5000 hallejujah/devops_app
```

## Unit tests

I wrote only one unit test for now using `pytest` for now.

More information is placed in `app_python/PYTHON.md`.

## Metric

Time of visits can be retrieved on `localhost:5000/visits` after the app is run.

## Contact

University mail: ro.zhukov@innopolis.university

Telegram: @Gimme_stipu_plz

GitHub: Hallejujah123
