# Reasoning behind the Python app

## Framework

For this application, I chose FastApi framework. In my opinion, it is a framework that allows to develop web apps fast.

## Practices used

1. I decided to use commonly-used ISO 8601 format with explicit timezone specification, which should make it easier to consume the API.
2. The solution is documented via auto-generated Swagger pages
3. Project code is split into different modules in a structured manner
4. FastApi Dependency Injection mechanism is used for easier unit-testing in the future

## Testing

For now, the testing is manual - on page refresh the time changes to the current time in Moscow Standard Time.
