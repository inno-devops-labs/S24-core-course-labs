# Project Description

## Framework Selection

For this project, I picked Flask. For Python, I think there are 3 goto solution- Django, FastAPI and Flask. Since, FastAPI is mainly for REST API and the project is to display time on screen, FastAPI was not a good choice. Django was way too heavy for this project. So, I picked Flask.

## Best Practices Followed

- The application was made as a python module so that unexpected import errors etc can be avoided.
- App route and logic is kept in separate files so that making changes get better.
- Adequate amount of type hinting is done to avoid runtime errors.
- Code is formatted according to PEP8 standards.
- Unittests are maintained for the application.
- Linter used to ensure code quality.
- `requirements.txt` to keep track of necessary packages.

## Ensuring Best Practices, Testing and Code Quality

- To have an unified coding styles, `black` was used
- To ensure static typing, `mypy` was used
- To ensure better code quality, `pylint` was used
- Tests are written for every utility function using `unittest` module.
- Docstrings are maintained for every function, module and class.
- Pre-commit hooks are used to run `black`, `mypy`, `pylint` and `unittest` before every commit.

![Screenshot](https://i.postimg.cc/sD97G5cR/image.png)
