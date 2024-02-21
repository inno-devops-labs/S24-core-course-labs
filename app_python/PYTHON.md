# "Time in Moscow" Web Application

## Framework Choice

This web-application is built with [Flask](https://flask.palletsprojects.com/en/3.0.x/) — lightweight WSGI web application framework.

I've chosen Flask, because:

- it's **simple to start** work with;
- it's one of the most **popular** Python web-frameworks;
- it has gained **trust** in the community;
- it is **open-source**;
- it has a built-in support for **Jinja templates**.

Since "Moscow Time Now" application is not a complicated project, the use of Flask made it possible to implement the functionality in a few lines of code, while leaving the opportunity to add new features to the application in the future.

## Best Practices

When implementing the web application, I followed the best practices:

- I created a [virtual environment](https://csguide.cs.princeton.edu/software/virtualenv) for my dependencies;
- I formatted code with [Black formatter](https://github.com/psf/black) and ensured that code follows the [PEP8 style guide](https://peps.python.org/pep-0008/);

I also manually tested the application locally on my machine.

## Unit Tests

Application unit tests are located at `tests` directory.

- I followed official PyTest and Flask guidelines on how to write the tests.
- I created `conftest.py` file, where I setup my tests and create fixtures used by test cases.
- `test_time.py` suit tests the functionality of the main logic, i.e. Moscow time generation.
- `test_server.py` tests the application itself, making sure it returns correct responses for the specific requests.
