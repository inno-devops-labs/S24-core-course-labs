# Flask Web Application Documentation

## Overview

This simple Flask web application displays the current time in Moscow.
The application is built using the Flask framework and utilizes
the datetime module for handling time and the pytz library for
handling time zones.

## Flask Installation

1. Ensure you have Python installed on your system. You can download it from `python.org`.

2. Install Flask using the following command:

    ```bash
    pip install flask
    ```

   Make sure to use a virtual environment for better isolation.
3. Install pytz using the following command:

    ```bash
    pip install pytz
    ```

## Flask Usage

1. Run the Flask application by executing the following command in the terminal:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://localhost:5000/` to view the current time in Moscow.

## Docker Installation

1. Install docker desktop from [official website](https://www.docker.com/products/docker-desktop/)

2. Run docker desktop

## Docker usage

Run commands from `app_python` directory

### Local run

1. Build stage

   ```bash
   cd app_python
   docker build -t app_python .
   ```

2. Run stage

   ```bash
   docker run -d -p 5000:5000 app_python
   ```

3. Open <http://localhost:5000/> and see the result

### Remote run

1. Pull stage

   ```bash
   docker pull doechon/app_python
   ```

2. Run stage

   ```bash
   docker run -d -p 5000:5000 doechon/app_python
   ```

3. Open <http://localhost:5000/> and see the result

## Dependencies

* Flask
* datetime
* pytz
* Docker
