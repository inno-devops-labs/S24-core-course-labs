# Kotlin Web Application

## Framework choice

I chose `Ktor` as a framework, since it is:

- Production ready
- Lightweight
- Flexible through plugins
- Has decent documentation and IDE support

## Best practices

- Following Kotlin coding conventions
- Usage of `OpenAPI`
- Usage of `Sonarlint` to analyze the code

## Testing

I tested the application manually using `Postman` and with 2 unit tests:

- That request is successful
- That time in response changes

### Unit testing

I created 2 unit tests:

- That `get` request is successful
- That time changes between requests

#### Best practices

- Tests are structured as `Arrange, Act, Assert`
- Tests are independent
- Test are executed automatically in CI workflow
