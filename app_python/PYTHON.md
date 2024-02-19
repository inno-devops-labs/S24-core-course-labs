## Chosen framework - FastAPI

For solving this lab's task I chose FastAPI framework. The choice was made due to several reasons:

- High performance

- Simplicity

- Follows Python principles

- Suits well for small and fairly simple projects


## Best practices

- Logging is implemented using `logging` library.
- Virtual environment is used during the development, all needed dependencies stored into `requirements.txt` file.
- Formatter was used to assert the code readability.
- Templates are separated from the main app and stored in `templates` folder.

## Testing

Implemented unit tests:

- Root endpoint returns `200` status code.
- Root endpoint returns correct time.
- Incorrect endpoint returns `404` status code.

Best practices:
- Tests are located separately from the rest of the code.
- Each test is isolated and independent.
- Each test is not complex and checks just one piece of functionality.
- `TestClient` is used to mock FastApi app.
- Edge cases are tested.

## Code quality

Code formatting was done using `Black` formatter, which assured the readability. The code quality was assured by using the best practices desribed above, the fault tolerance is achieved by the error handling.
