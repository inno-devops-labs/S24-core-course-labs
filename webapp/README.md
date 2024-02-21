# Moscow Time Django Web Application

## Overview

This Django web application provides an API endpoint that returns the current time in Moscow. It uses the `Django` framework along with the `pytz` library for handling time zones.

## Table of Contents

- [Features](#features)
- [Prerequisities](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example response](#example-response)
- [Docker](#docker)

## Features

- Provides a RESTful API endpoint to retrieve the current Moscow time.
- Follows best practices for Django web application development.

## Getting Started

### Prerequisites

- Python 3.x
- `Django` framework
- `pytz` library

### Installation

1. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the Moscow time API endpoint:

    - URL: http://localhost:8000/moscow-time/
    - Method: GET
    - Response: JSON object containing the current Moscow time.

### Example Response

```json
{
  "moscow_time": "2024-02-05 12:34:56 MSK"
}
```

## Docker

### Building the Docker Image

To build the Docker image for this application, follow these steps:

1. Navigate to the root directory of the project.
2. Run the following command:
    ```bash
    docker build -t webapp .
    ```

### Pulling the Docker Image

If you prefer to pull the Docker image from a registry instead of building it locally, you can use the following command:

```bash
docker pull grisharybolovlev/webapp:v1.0
```

### Running the Docker container

To run the Docker container for this application, execute the following command:

```bash
docker run -p 8000:8000 webapp
```

This command will start the Django application inside a Docker container, and you can access it at http://127.0.0.1:8000 in your web browser.
