# Python Web Application

## Framework choice

I have chosen `Flask` framework since it is one of the most wide-used python web frameworks.
Flask has all possible functionality that may be used in web development.

## Best practices

+ I have followed one best practice: KISS. This is the most simple and robust example of required server.
+ Code is formatted with compliance to PEP 8 using Pycharm formatter.
+ `pylint` was used to check code quality.

## Testing

This application was tested by opening service page with Moscow time in browser.

# Docker

## How to build Python Web Application image?

```bash
cd app_python
docker build -t masterlogick/devops-py-img .
```

## How to pull Python Web Application image?

```bash
docker pull masterlogick/devops-py-img
```

# How to run Python Web Application?

```bash
docker run -p 8080:8080 masterlogick/devops-py-img
```

# Testing

As best practices I have mocked server using flask `test_client`, applied fixtures and split unit and service tests.

## Unit Testing

Here I have created unit tests that validate returned time for:

1. Iso time format
2. Timezone
3. Difference with system time

## Service testing

This tests cover index endpoint:

1. Return code
2. Content type
3. Content length and format
