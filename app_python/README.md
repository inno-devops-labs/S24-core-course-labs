## Prerequisite

Install Python 3.12
Install Poetry - `$ curl -sSL https://install.python-poetry.org | python3 -`

# How to run an app?

Run in terminal: `$ poetry run uvicorn src.app:app --port <port>`

# How to run tests?

Run in terminal: `$ poetry run pytest`

# How to check test coverage?

Run in terminal: `$ poetry run pytest --cov=src`

# How to pull this Docker image?

Run in terminal: `$ docker pull brutaljesus/devops_lab_2`

# How to build this Docker image?

Run in terminal: `$ docker build -t devops_lab_2 .`

# How to run this Docker image?

If you have pulled it: `$ docker run -p 8000:8000 brutaljesus/devops_lab_2`
Or if you have built it manually: `docker run -p 8000:8000 devops_lab_2`
