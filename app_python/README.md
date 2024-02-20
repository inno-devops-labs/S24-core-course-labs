![Deploy badge](https://github.com/GuzelZakirova/devops-course/actions/workflows/app_python_ci.yml/badge.svg)

# Application for displaying the Moscow time

## Installation

Install the dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python app_python\\src\\main.py
```

## Docker

To pull docker image:

```bash
docker pull guzelzakirova/moscow-time-app:1.0.0
```

To run docker image:

```bash
docker run -p 8000:8000 --name moscow-time-app guzelzakirova/moscow-time-app:1.0.0
```

## Unit Tests

To run tests:

```bash
pip install pytest
pytest
```

## CI workflow

- Build, lint and test
  - Pylint for linting
  - Pytest for testing
