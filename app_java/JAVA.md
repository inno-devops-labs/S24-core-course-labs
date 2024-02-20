# Java Web Application

## Framework choice

I have chosen `SpringBoot` framework because of its popularity in Java backend
development. Moreover, I decided to use a simple `maven` build system for this
project (`gradle` is a way more complicated)

## Best practices

- I have followed KISS principle which is the most suitable for simplest
  applications.
- Application has a simple `application.properties` configuration
- I have configured `pre-commit` hooks (check `.pre-commit-config.yaml` file)
- Code is formatted and linted by Intellij Idea built-in tools.
- `markdownlint` is used for checking documentation style.

## Testing

This application was tested using unit tests and `JUnit 5.7` library. There are
3 tests:

1. Checks availability of the application
2. Checks that non-broken HTML is returned
3. Checks that displayed time is correct excluding milliseconds
