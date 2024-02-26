# Python Web Application

## Overview

This Python web application provides current time information. It's built with FastAPI and designed with best practices in mind for maintainability, testing, and performance.

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

First of all, you need to create virtual python envionment

```bash
python -m venv venv
```

Next, install all dependencies required for the project

```bash
venv/bin/pip install -r requirements.txt
```

### Runnig the Application

You can run the application by the following command

```bash
venv/bin/uvicorn main:app --reload
```

Next, navigate to `http://127.0.0.1:8000/` and check current moscow time!

### Testing

To run the tests, execute:

```bash
venv/bin/pytest
```

