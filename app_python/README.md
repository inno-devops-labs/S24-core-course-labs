# Flask Web Application
[![app python](https://github.com/itoqsky/S24-core-course-labs/actions/workflows/main.yml/badge.svg?branch=lab3)](https://github.com/itoqsky/S24-core-course-labs/actions/workflows/main.yml)

This simple Flask web application displays the current time in Moscow. It serves as a demonstration of best practices in web development.

## Installation:

1. Clone the repository:

   ```bash
    git clone <repository_url>
    cd app_python
    pip install -r requirements.txt
    python3 app.py
    python3 -m unittest test_app.py

## Docker

1. Building the Docker Image
   
   ```bash
   docker build -t python-app .

2. Pulling the Docker Image
   ```bash
   docker pull itoqsky/python-app


3. Running the Docker Image
   ```bash
   docker run -p 5555:5555 python-app


