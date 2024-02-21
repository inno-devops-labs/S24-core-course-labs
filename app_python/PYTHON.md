# Python Web Application

## Framework

[Flask](https://flask.palletsprojects.com/) is used as a framework because it is not only
lightweight (in comparison with Django), but also scalable and flexible (in comparison with FastAPI).
It is also widely used and has rich documentation.

## Testing

### Unit tests

Unit testing was done with [pytest](https://docs.pytest.org/en/7.4.x/contents.html). The tests performed are:

- Checking that the page mentions 'Moscow';
- Verifying the time format.

Some tests were also performed manually, for instance via page refreshing.

## Best Practices Applied

- The code is written following **official Flask documentation**;
- **Virtual environment** is used to isolate dependencies;
- **GitHub** is used as **VCS** to track changes and project history;
- PyCharm built-in **linter** is used to achieve style consistency;
- Tests are clear and self-explanatory, performed via pytest.

## Coding Standards

The following code standards are followed in the development process:

- Meaningful naming;
- Proper indentation;
- Comprehensive coding style.

## Code Quality

Code quality was ensured via PyCharm code inspection.
