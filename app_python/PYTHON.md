## Choice of framework


I chose ``Flask`` for this project due to following reasons:
 - It is well-suited for small projects:)
 - It is easy to insert content into HTML templates using it.
 - It has build-in development server for testing.

## Best practices

- Logging: use ``logging`` library for printing logs into ``app.log`` file
- ``.gitignore``: use it to stash logs.
- Error handling: add ``error.html`` template to render it in case of errors.
- Testing: wrote test for validating if rendered time is correct using ``unittest`` library.
- ``requirements.txt`` with dependencies by <code>pip freeze > requirements.txt</code> command.
- Store all HTML templates into separate folder ``templates``
- Follow Python's PEP 8 style guide for code consistency.

## Testing

- File ``test_app.py`` contains unit test which validates the rendered time by calculating the actual time during the test and compares them.

## Code quality

- I used ``Pylint`` linter for code formatting.

