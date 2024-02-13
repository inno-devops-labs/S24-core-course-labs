# Moscow Time WebApp

## Overview

This is a very simple Python web application built with Flask to display the current time in Moscow.

## Getting Started

### Prerequisites

- Python
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Orillio/S24-core-course-labs.git
   ```

2. Navigate to the project directory:

   ```bash 
   cd S24-core-course-labs/app_python
   ```
2. Install the required dependencies
   ```bash 
   pip install -r requirements.txt
   ```

Usage

## Run the Flask application:

```bash
python app.py
```
Open your web browser and visit http://127.0.0.1:5000/ to view the current time in Moscow.

## Testing

Run the provided unit tests to ensure the application is working correctly:

```bash
python -m unittest test_app.py
```

## Building and running docker

To run the application as docker container:

```bash
docker pull orillion1/lab2
```

```bash
docker run -p 5000:5000 lab2
```

The application will be accessible at `127.0.0.1:5000`