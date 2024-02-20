# Project environment

## Best practices

- use linters for consistent styling
- use 'constants' with a speaking name
- write requirements file with dependencies and their versions
- write README file with a description of the project and installation process
- use virtual environment for isolated development
- brief comments in code
- add .gitignore to avoid uploading unnecessary files that can be retrieved from 

## Tech stack

### Web framework

As a WEB framework, I have chosen Flask.

#### Pros

- Very lightweight
- Easy routing
- Can use HTML templates, easily understandable

#### Cons

- May perform worse if the app grows too much
- Requires additional server side

### Server

Used Gunicorn for server side

### Linters

I used:

- `pymarkdown` for MarkDown linting
- `isort` for linting imports in .py files
- `black` for linting .py files after isort

Isort and Black are useful as they are not only linters, but also formatters.

### Unit test

I used `pytest` for running tests.

Now, there is only one test. It tests whether app is running or not.

Best practices:

- Isolated tests (in a separate directory).
- Fixtures for tests.
- Good and self-secribing names.
- Simple tests.
- Test only one unit of functionality.