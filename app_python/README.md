[![Flask App CI](https://github.com/RoukayaZaki/S24-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/RoukayaZaki/S24-core-course-labs/actions/workflows/ci.yml)
# Python Web Application

This is a Python web application built using the Flask framework to display the current time in Moscow.

## Features

- Displays the current time in Moscow.
- Modern and beautiful UI using Bootstrap.
- Simple and lightweight.

## Setup

1. Clone the repository:

```
git clone https://github.com/RoukayaZaki/S24-core-course-labs/tree/lab01
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

4. Open your web browser and navigate to `http://localhost:5000/` to view the application.

5. Unit Tests
To run the tests:
```
pytest
```
## Project Structure

- `app.py`: Main Flask application file containing route definitions.
- `templates/`: Directory containing HTML templates.

## Dependencies

- Flask: Micro web framework for Python.
- pytz: World timezone definitions and utilities.

## Docker

### Description:

The application is containerized using Docker for easy deployment and management.

### Build Instructions:

To build the Docker image, run the following command in the root directory of the project:

```bash
docker build -t <image_name> .
```
### Run Instructions

To run the Docker container locally, execute the following command:

```bash
docker run -p 5000:5000 <image_name>
```

Make sure to replace \`<image\_name>\` with the desired name for your Docker image.

### Pull Instructions

If you prefer to pull the pre-built Docker image from a registry, you can use the following command:

```bash
docker pull roukayazaki/devops-lab02:latest
```
### CI
The workflow is done using Github actions
The workflow includes:
- building, testing and linting job
- building and deploying image on dockerhub
- checking security valnurabilities with Synk
The workflow uses ubuntu as a base for every job