# Lab 1

### Framework choice

I chose the minimalistic framework FastAPI because it is well-designed for small projects. It is easy to start a project
using [**FastAPI**](https://fastapi.tiangolo.com/). In our case with this framework we can put everything in one file
because we have a tiny codebase.

The other point is that we do not have any redundant parts of codebase with FastAPI, so it is much easier to analyze
comparing to **[Django](https://www.djangoproject.com/)** or **[Flask](https://flask.palletsprojects.com/en/3.0.x/)**.
Moreover, we do not need any separate services such as codebase. Therefore, the
configuration will be minimal.

### Testing

I tested my application manually because automated tests are not required in this assignment.
I refreshed page several times in different moments, and I ensured that the time was always correct.

### Best practices

* #### Standards:
  In my application I followed the standards of python code such as PEP8. I avoided all the code smells, followed the
  restricted length of lines up to 79 chars. I also documented my code properly.
* #### Linters:
  For linting I used Pylint to ensure that my code follows the common best practices.
* #### Formatters:
  For formatting, I used the Black and Isort to structure the code properly, follow the restricted length of lines and
  sort the imports.