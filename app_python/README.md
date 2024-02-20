![python workflow](https://github.com/Probirochniy/S24-core-course-labs/actions/workflows/app_python.yml/badge.svg)

# Moscow time app

## Description

A simple FastAPI app that displays Moscow time.

## Getting started

1. Install all required Python packages:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python main.py
```

The application will start locally on port `8000`. You can access it by navigating to `http://127.0.0.1:8000` in the web browser.

## Endpoints

A single endpoint is currently present:

- `/` (GET): Returns an HTML page with the current Moscow time.

## Templates

Jinja2 templates are used, stored in `templates` folder.

- time.html - A simple html template with the large text in the center.

## Logging

The application logs requests, returned values and errors in `app.log` file.

## Error handling
If an error occurs, the app will return a 500 status code and log an error.

## Docker

To build an image, run the following command in `app_python` directory of the project:

```bash
docker build -t moscow-time-app .
```

Alternatively, you can pull the image from `dockerhub`:

```bash
docker pull damirafliatonov/moscow-time-app:latest
```

To run the image, run the following command:

```bash
docker run -p 8000:8000 moscow-time-app
```

After that, the application will be accessible at `http://localhost:8000/` in the web browser.

## Unit tests
Unit tests are located inside the `tests/unit/test.py` file. They can be run using `pytest`:

```bash
pytest tests/unit/test.py
```

## CI workflow

At push/pull request into `app_python`, workflow starts via github actions. It runs dependencies check, linter and tests of the project. Moreover, the docker image is built and pushed into the Dockerhub.
