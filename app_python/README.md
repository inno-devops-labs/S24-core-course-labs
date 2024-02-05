# Python Moscow Time Web Application
![tests](https://github.com/slry/S24-core-course-labs/actions/workflows/python_tests.yml/badge.svg?branch=lab1)

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
To run application
```bash
cd app_python
uvicorn main:app
```
Or
```bash
cd app_python
python3 -m main
```
Go to http://127.0.0.1:8000
