# Python Web Application

## Framework choice

I chose `Sanic` as a framework, since it is:

- Production ready
- Fast and lightweight
- Flexible through `Sanic Extensions`
- Has decent documentation

## Best practices

- Usage of virtual environment
- Usage of `OpenAPI`
- Usage of `Pylint` to analyze the code

## Testing

I tested the application manually using `Postman`

### Unit testing

I created 2 unit tests:

- That `get` request is successful
- That time changes between requests

#### Best practices

- Tests are structured as `Arrange, Act, Assert`
- Tests are independent
- Test are executed automatically in CI workflow
