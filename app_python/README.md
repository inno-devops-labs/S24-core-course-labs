## Description

Simple Python web application that shows current time (Moscow timezone).

### Setup

Make sure you have `make` tool on your Unix OS; enter the `app_python` folder and setup enviroment with `make init`. It will create `venv` with all installed needed dependencies. Also it will setup `pre-commit` to check commits (uses `.pre-commit-config.yaml`).

Keep in mind, if you want to act in `venv`, write `source venv/bin/activate` in folder terminal.

### Run

Run web server use `make run` command or `bash start.sh` in `venv` terminal. Web application with formatted Moscow time (and date actually) will be available on `http://0.0.0.0:8000/`. Try to refresh page to update info.

### Tests

To run tests use `make test` or `pytest tests` command.

### Following code style

Format features (linters + codebase style) can be run via `make format`, and static typecheck with `make typecheck` commands.
