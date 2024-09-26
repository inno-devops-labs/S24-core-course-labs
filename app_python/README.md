# Python Web Application

## Description

This is simple Python web application that displays the current time in Moscow.
To develop the app, I used the FastAPI framework, `datetime` to fetch the time and `pytz` to get the desired time zone.

## Start

### Installation process

1. Clone the repository: `git clone https://github.com/Alyona-art/S24-core-course-labs.git`
1. Change into the project directory: `cd app_python`
1. Install python packages `pip install -r requirements.txt`

### Usage

Run the application using the following command

`uvicorn main:app`

The application will be accessible at http://127.0.0.1:8000

## Testing

Run the tests using the following command

`unittest tests/time_tests.py`
