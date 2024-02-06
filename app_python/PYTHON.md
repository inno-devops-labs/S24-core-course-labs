# Project Description

## Framework Selection

For this project, I selected FastAPI. Considering the landscape of Python web frameworks, Django, Flask, and FastAPI stand out as the primary options. Django, with its comprehensive feature set, is typically suited for larger applications, making it somewhat excessive for simpler projects. Flask offers a lightweight and flexible approach, ideal for smaller applications but lacking some of the more advanced features needed for high-performance API development. FastAPI, while often associated with REST API development, was chosen for its simplicity, performance benefits, and built-in support for asynchronous programming. These features make FastAPI an excellent choice for efficiently serving web pages and handling backend logic, even for applications primarily focused on content display rather than REST APIs.


## Best Practices Followed

- The application is structured as a Python package, enhancing modularity and preventing import errors.
- Application routing and business logic are separated into distinct modules for improved maintainability.
- Extensive use of type hints ensures more predictable behavior and reduces the risk of type-related errors.
- Adherence to PEP8 standards for Python code formatting is strictly enforced.
- Unit tests are implemented to verify the application's functionality and robustness.
- A linter is utilized to maintain code quality across the project.
- Dependency management is facilitated through a `requirements.txt` file, ensuring a consistent development and deployment environment.

## Ensuring Best Practices, Testing and Code Quality
- `black` is used as the code formatter to achieve consistent coding styles throughout the project.
- Static type checking is conducted with `mypy`, enhancing code reliability and maintainability.
- `pylint` is employed to identify potential code quality issues, ensuring adherence to best practices.
- Comprehensive tests for all utility functions and endpoints are written using FastAPI's test client, facilitating thorough    validation of application behavior.
- Docstrings are present for each function, module, providing clear documentation of the project's codebase.
- Pre-commit hooks are configured to automatically run `black`, `mypy`, `pylint`, and `tests` through FastAPI's test client before each commit, ensuring that only code that meets the project's quality standards is committed to the repository.

## Iterative Code Quality Development
[![Initial.png](https://i.postimg.cc/mgfcwh0d/image.png)](https://postimg.cc/56gN999v)
[![Second.png](https://i.postimg.cc/zvQxMTnH/image.png)](https://postimg.cc/RJc1J6pv)
[![Final.png](https://i.postimg.cc/xTRvcvkv/image.png)](https://postimg.cc/ykDgGSyx)