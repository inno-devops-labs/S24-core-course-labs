# Python Web Application - Moscow Time Display

## Overview
This Python web application is designed to display the current time in Moscow. It's built with the Flask framework, offering a simple interface that refreshes to update the time displayed.

## Features

- Displays the current Moscow time in a simple web interface.
- Time updates on page refresh.

## Prerequisites
Before running this application, ensure you have the following installed:

- Python 3.x
- Flask
- pytz (for timezone handling)

## Installation
Clone the repository to your local machine:

```
git clone https://github.com/ananastya1/S24-core-course-labs
cd app_python
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the Application
To run the application, execute:

```
python app.py
```
Navigate to http://127.0.0.1:5000/ in your web browser to view the application.

## Testing
Ensure all tests pass by running:

```
python -m unittest discover
```

For test coverage, run:

```
coverage run -m unittest discover
coverage report
```
