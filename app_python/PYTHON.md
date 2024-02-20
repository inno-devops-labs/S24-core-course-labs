# Overview of best practices & framework choice

## Best practices

- Type hints to help maintain the app
- [docstrings](https://www.python.org/dev/peps/pep-0257/)
- [pytest](https://docs.pytest.org/en/8.0.x/) to test the app
- Code is formatted according to PEPs

## About framework choice

I chose [FastAPI](https://fastapi.tiangolo.com/) because the following:

- It's fast and simple to code
- It's widely [used](https://fastapi.tiangolo.com/#opinions) in industry
- It's blazing [fast](https://fastapi.tiangolo.com/#performance)

## Unit testing

I use [pytest](https://docs.pytest.org/en/8.0.x/) to test the app

### Test description

- `test_time_changes` checks that time is really updated as it was required in the task
- `test_main200` checks that `/` path returns 200 HTTP code
- `test_nonexistent404` checks that non-existent path returns 404 HTTP code

### Tests best practices

- **Separate test functions**: Each test is defined as a separate function, which helps in organizing and running individual tests independently.
- **Test Isolation**: Each test function is isolated and doesn't rely on the state of other tests. This is important to ensure that tests remain independent, and one test's failure doesn't impact the execution of others.
- **Using a test client**: The `TestClient` class from `fastapi.testclient` is used to create a test client for the FastAPI application defined in main.py. This allows for easy testing of HTTP requests and responses. This is the recommended approach for testing FastAPI applications.
