# Reasoning behind the Python app

## Framework

For this application, I chose FastApi framework. In my opinion, it is a framework that allows to develop web apps fast.

## Practices used

1. I decided to use commonly-used ISO 8601 format with explicit timezone specification, which should make it easier to
   consume the API.
2. The solution is documented via auto-generated Swagger pages
3. Project code is split into different modules in a structured manner
4. FastApi Dependency Injection mechanism is used for easier unit-testing in the future

## Testing

### Unit tests

The unit tests are done via Pytest and some FastApi features.
In contrast to integration tests, unit tests verify just the separate moduls
(in this case, controller and the singular service)

Some practices used:

1. Separate requirements file for tests, so that these dependencies are not included in the built docker image
2. Application and tests are separated into different folders, so that we can not include tests when building docker
   image
3. These tests are not very useful because of the app simplicity, but I used FastApi dependency override feature to mock
   datetime retrieval in controller tests, which could be useful for mocking some external services
4. CI runs tests automatically


## CI

CI includes

1. Testing - python is installed with the dependencies
   - linting is run via `ruff`
   - unit tests are run via `pytest`
2. Docker build & push
   - only on push to main
   - login, build and push as `:latest`
3. Security - using `snyk`