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

This application was tested manually by comparing the outputs with this
[site](https://www.timeanddate.com/worldclock/russia/samara)
