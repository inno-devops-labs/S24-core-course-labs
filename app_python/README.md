## Prerequisite

Install Python 3.12
Install Poetry - `$ curl -sSL https://install.python-poetry.org | python3 -`

# How to run an app?

Run in terminal: `$ poetry run uvicorn src.app:app --port <port>`

# How to run tests?

Run in terminal: `$ poetry run pytest`

# How to check test coverage?

Run in terminal: `$ poetry run pytest --cov=src`

