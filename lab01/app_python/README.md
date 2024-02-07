# Python Web-app

## Overview

This Python web application is designed to display the current time in Moscow, utilizing the FastAPI framework. It provides a simple and intuitive interface for users to access the current time in the specified timezone.

## Installation & Running

To install and run the application locally, follow these steps:

Clone the repository to your local machine:

```bash
pip install -r requirements.txt
```

Run with 
```bash
PYTHONPATH="app_python" uvicorn app:app --reload
```

Now app will be accessible at http://127.0.0.1:8000/

## Testing

Running tests:

```bash
pytest
```