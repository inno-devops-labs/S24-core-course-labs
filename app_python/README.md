# FastAPI Time Display App

This web application displays the current time in Moscow, developed using the FastAPI framework and Python.

## Table of Contents

- [FastAPI Time Display App](#fastapi-time-display-app)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation Steps](#installation-steps)

## Installation

### Requirements

- Python 3.8 or higher
- `pip` package manager

### Installation Steps

- Clone the repository to your local machine:

```bash
git clone https://github.com/Ejedavy/S24-core-course-labs.git
```

- Navigate to the `app_python` folder

```bash
cd app_python
```

- Create and activate a virtual environment (Linux)

```bash
python3 -m venv venv
source venv/bin/activate
```

- Create and activate a virtual environment (Linux)

```bash
python -m venv venv
.\venv\Scripts\activate
```

- Install the required packages

```bash
pip install -r requirements.txt
```

- Run the application

```bash
uvicorn app:app --reload
```

The application will be available at [localhost:8000](http://localhost:8000/)
[![LocalHost.png](https://i.postimg.cc/QCPrb9C0/image.png)](https://postimg.cc/xNK7jdKz)
