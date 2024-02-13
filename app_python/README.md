# App Python

This repository contains a Flask-based web application designed to display the current time in Moscow. It serves as an example of implementing best practices in web application development with Python.

## Overview

The application is straightforward, with its primary function being to show the current Moscow time to the user. This functionality is implemented using the Flask framework and the `pytz` library for accurate timezone handling.

## Local Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:
```bash
git clone https://github.com/LaithAlebrahim/S24-core-course-labs.git
```
## Usage

To use this application, run the following commands:

```bash
cd app_python
```

2. **Install Dependencies**:
```bash
pip3 install -r requirements.txt
```
3. **Run the Application**:
```bash
python3 app.py
```
4. **View in Browser**:
Open your browser to http://localhost:5000/ to see WEB APP

## MSK Time Setup

The application uses the `pytz` library to handle timezone information, ensuring the displayed time is accurate for the Moscow timezone.