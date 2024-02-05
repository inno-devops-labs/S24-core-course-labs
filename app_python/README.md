# Moscow Time Web App

This Python web application displays the current time in Moscow.

## Features

- Lightweight web app built with Flask.
- Utilizes `pytz` for accurate time zone handling.
- Follows PEP 8 coding standards for clean and readable code.
- Includes a simple unit test to ensure time format correctness.

## Setup

It is advisable to create a virtual environment before proceeding with the installation. [Refer to the guide here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and visit http://127.0.0.1:8000 to see the current time in Moscow.

## Testing
Run the unit test to ensure the time format is correct:
```bash
python -m unittest tests/test_app.py
```

## Dependencies
* Flask
* pytz
* pytest
