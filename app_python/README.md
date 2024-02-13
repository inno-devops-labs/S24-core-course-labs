# Python Moscow Time Web Application
![tests](https://github.com/slry/S24-core-course-labs/actions/workflows/python_tests.yml/badge.svg?branch=lab2)
![docker](https://github.com/slry/S24-core-course-labs/actions/workflows/docker_build_python.yml/badge.svg?branch=lab2)

## Overview
Simple App that shows current Moscow Time and Date

## Requirements
- Python 3.9 or higher
- pip package manager

## Installation
- Clone this repository
```bash
git clone https://github.com/slry/S24-core-course-labs.git -b lab1
cd S24-core-course-labs
cd app_python
```
- Create Python Virtual Enviroment (venv)
```bash
python3 -m venv .venv
source ./.venv/bin/activate
```
- Install requirements
```bash
pip install -r requirements.txt
```

## Usage
- Run application
```bash
cd app_python
uvicorn main:app
```
- Or alternatively
```bash
cd app_python
python3 -m main
```
Go to http://127.0.0.1:8000

## Usage Docker
- Pull image
```bash
docker pull slry/python_moscow_time
```
- Run Container
```bash
docker run -p 8080:8080 slry/python_moscow_time
```

Go to http://127.0.0.1:8080
