# Python Web Application

![CI](https://github.com/Mierley/S24-core-course-labs/.github/workflows/python-app.yml/badge.svg)

## Overview

This is a simple Python web application that displays the current time in Moscow. The application is built using the Flask framework, following best practices and coding standards.

## Features

- Displays the current time in Moscow.
- Includes unit tests for critical components.
- Organized code structure for better maintainability.

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mierley/S24-core-course-labs/tree/main/app_python
   cd app_python

2. Install dependencies:
    ```bash
   pip install -r requirements.txt

   
### Docker
1. Build your own image
   ```bash
   docker build -t mierley4041/devops-flask .
   ```
   
   Or pull from DockerHub
   ```bash
   docker pull mierley4041/devops-flask:latest
   ```
   
2. Run container
   ```bash
   docker run -dp 5000:5000 mierley4041/devops-flask:latest
   ```
   
3. App will be available on `127.0.0.1:5000`

### Unit Tests

This project includes unit tests to verify the functionality of key components. To run the unit tests, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Navigate to the `tests` directory.
4. Run the following command to execute the unit tests:

```bash
python -m unittest test_app.py
```
OR

```bash
python tests/test_app.py
```