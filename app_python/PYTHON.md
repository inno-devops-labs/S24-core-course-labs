# Python Web Application

## Framework choice

I have chosen `Flask` framework since it is one of the most wide-used python web
frameworks. Flask has all possible functionality that may be used in web
development.

## Best practices

- I have followed KISS principle which is the most suitable for simplest
  applications.
- I have configured `pre-commit` hooks (check `.pre-commit-config.yaml` file)
- Code is formatted by `black` formatter, linted by `pylint`, statically checked
  by `mypy`.
- `markdownlint` is used for checking documentation style.

## Testing

This application was tested using unit tests and `pytest` library. There are 3
tests:

1. Checks availability of the application
2. Checks that non-broken HTML is returned
3. Checks that displayed time is correct excluding milliseconds
