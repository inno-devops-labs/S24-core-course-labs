# APP PYTHON PTIME

## Overview

Runs server which returns the MSK tz time. Source code is in `ptime` folder

## Prepare local environment

```bash
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run the app

```bash
python ptime/main.py
```

## Run tests

```bash
pytest
```

## In Docker

Either pull docker image

```bash
docker pull legolass322/devops:python
```

Either build it yourself

```bash
docker build -t devops .
```

Then to run app
```bash
docker run -p <PORT>:8080 devops
```