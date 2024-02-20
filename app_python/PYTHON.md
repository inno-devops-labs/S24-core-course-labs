# Framework choice

I have chosen **FastAPI** since it is a easy-to-use framework, that can we used very fast if I have such little tasks as this one. Django could take much more time to set up.

Moreover, **FastAPI** supports asynchronous Python. Therefore, if we will want to add some `async` functions, this will not be a big deal.

# Best practices

## Code

### Style guide

I used PEP8 style guide in order to make code more beautiful. If I forget something, `black` this for me.

Usage: `$ poetry run black .`
### Type hints

I used type hints in order to make less mistakes. Moreover, `mypy` helped me to recheck for the types correction in my code.

Usage: `$ poetry run mypy .`
### Business logic isolation

I isolated the logic of getting time and it's string representation from the FastAPI controller. It will be not difficult to change the logic on demand.
## Testing

### Unit and integration tests

I tested my app both from the perspective of all components and from the perspective of the app (unit- and integration- testing respectively).

I created 2 unit tests:
- `test_get_current_moscow_time`: checks that `get_current_moscow_time` function returns a `datetime` object
- `test_get_human_readable_time`: checks that `get_current_moscow_time` functions returns a specific human-readable format

### Tests running

I used `pytest` in order to run all my tests.

Usage: `$ poetry run pytest`
### Separate tests from the app

I separated tests from the app code in order to clearly distinguish between them and comfortably check test coverage.
### Test coverage

I used `pytest-cov` in order to check how many percent of code lines I have tested.

Usage: `$ poetry run pytest --cov=src`
