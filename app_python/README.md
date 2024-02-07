# Current Moscow Time - FastAPI Web Application

This is a simple Python web application developed using FastAPI. The application displays the current Moscow time in the browser and updates continuously.

## Getting Started

These instructions will get a copy of the project running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.6+
- pip

### Installation & Usage

Clone the repository to your machine

```shell
git clone git@github.com:vladdan16/S24-core-course-labs.git
```

Navigate into the project directory

```
cd S24-core-course-labs/app_python
```

Install the required modules

```shell
pip install -r requirements.txt
```

Start the server

```shell
uvicorn app:app --reload
```

Then open your browser and go to http://localhost:8000/ to see the current time in Moscow. 

## Running the Tests

To run the tests type the following command:

```shell
pytest
```

