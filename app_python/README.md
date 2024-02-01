# Current Moscow time web application documentation

## Overview

This is a simple Python web application built using Flask. Its main feature is to display the current time in Moscow.

## Prerequisites

Make sure you have Python and Docker installed on your system.

## Local installation

* Clone the repository to your local machine:

```
git clone https://github.com/y0szx/devops.git
```

* Go to the `app_python`:

```
cd app_python
```

* Create virtual environment:

```
python3.11 -m venv env
source env/bin/activate
```

* Install dependencies:

```
pip install -r requirements.txt
```

* Run the application:

```
python main.py 
```

* Go to https://127.0.0.1:5000 to view the result.

## Docker

This application is containerized using Docker to ensure consistency and portability across different environments. The
Docker image includes all the necessary dependencies to run the application.

* ### How to build?

To build image locally go to app_python directory and use:

```
docker build -t app_python .
```

To run locally use:

```
docker run -p 5000:5000 app_python
```

* ### How to pull?

To pull the image from the Docker Hub use:

```
docker pull yuszx/app_python
```

* ### How to run?

To run pulled image use:

```
docker run -p 5000:5000 yuszx/app_python
```

Go to https://127.0.0.1:5000 to see the result.