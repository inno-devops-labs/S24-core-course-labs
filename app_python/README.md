# FastAPI Time Display App
![CI Python](https://github.com/Ejedavy/S24-core-course-labs/actions/workflows/ci_python.yaml/badge.svg)
This web application displays the current time in Moscow, developed using the FastAPI framework and Python.

## Table of Contents

- [FastAPI Time Display App](#fastapi-time-display-app)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation Steps](#installation-steps)
    - [Docker](#docker)
      - [For AMD chips](#for-amd-chips)
      - [For ARM chips](#for-arm-chips)
  - [CI](#ci)

## Installation

### Requirements

- Python 3.8 or higher
- `pip` package manager

### Installation Steps

- Clone the repository to your local machine:

```bash
git clone https://github.com/Ejedavy/S24-core-course-labs.git
```

- Navigate to the `app_python` folder

```bash
cd app_python
```

- Create and activate a virtual environment (Linux)

```bash
python3 -m venv venv
source venv/bin/activate
```

- Create and activate a virtual environment (Linux)

```bash
python -m venv venv
.\venv\Scripts\activate
```

- Install the required packages

```bash
pip install -r requirements.txt
```

- Run the application

```bash
uvicorn app:app --reload
```

The application will be available at [localhost:8000](http://localhost:8000/)
[![LocalHost.png](https://i.postimg.cc/QCPrb9C0/image.png)](https://postimg.cc/xNK7jdKz)



### Docker

This repository contains a Dockerfile which you can build the image from or you could pull the image from docker hub.

To build the image, use the following command:

```bash
docker build -t app_python .
```

To pull the image from the Docker Hub, use the following command:

```bash
docker pull ejedavid/app_python:latest
```

After building or pulling the image, the container can be run with the following command:

#### For AMD chips

```bash
docker run -p 8000:8000 app_python
```

#### For ARM chips
```bash
docker run -p 8000:8000 --platform linux/amd64 python_app
```

The application will be available at [localhost:8000](http://localhost:8000/)

## Visits
I stored the visits count to the "/" and "/visits" routes using a file "visits.txt" to maintain consistency I used async-await.

[![image.png](https://i.postimg.cc/L8PH8g59/image.png)](https://postimg.cc/21zpH6nM)

I initialised/reset the visit count everytime there is a startup event fired and I listened via `@app.on_event("startup")`

## CI
A CI workflow is contained in the `.github/workflows/ci_python.yaml` file. This workflow lints and tests the application, checks code vulnerability using SNYK, and builds and pushes docker image. Workflow is triggered only if the there is a change in the `app_python` directory or the workflow file itself.

The CI workflow contains 3 jobs. Each job has a specific set of tasks to perform:

- Build: This job lints and tests the application
- Security: This job checks code vulnerability using SNYK
- Docker: This job builds and pushes the docker image to the Docker Hub. The job is carried out only if the previous jobs are successful.