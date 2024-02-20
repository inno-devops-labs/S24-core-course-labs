## Framework choice justification
I chose FastAPI as a framework for this python application, because it introduces simplicity in development API and also provides an opportunity to create API documentation automatically.

## Best practices 
1. Separation of business logic from other parts, which is essential for future scaling of the application.
2. Usage of linting (flake8, black formatter) for consistancy with PEP8 standard.
3. Unit testing for clarifying the corretness of different parts of application independently.
4. Usage of virtual environment to separate packages from global environment and be consistent with the packages' versions.

## Testing

**Unit tests**
Unit testing is based on mock function that changes behaviour of datetime.now() function to display time is passed to it.

1. Unit test to check that local (MSK) time is preserved the same. 
2. Unit test to check that non-local (NY) time is converted to MSK time.

**Best practices**
1. Enhacing structure by separating tests and fixtures.
2. Fixtures usage.
3. Using pytest parametrization for the same testing behaviour
4. Using global constants as testing data.
5. Testing CI step is used every time `push` or `PR` action is happened. Therefore, issues can be noticed right away.
6. Usage of Pytest framework for managing the testing.