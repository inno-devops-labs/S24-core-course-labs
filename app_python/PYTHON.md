# Solution description

## Best practices I applied

- PEP styling
- "Entry point" `if __name__ == '__main__'`
- `requirements.txt`

## Why I chose Flask

### Pros

- Easy to use
- Lightweight
- Good documentation

### Cons

- Bad for large apps (but it's not a problem for this task)

## Linters

- `Python` vscode extension
- `markdownlint` vscode extension

## Unit tests

### Added tests

1. Checking if the function `get_moscow_time` returns time in the correct format
2. Checking if the flask app returns 200 for the `/` route

### Best practices

- used pytest
- folder structure
- `__init__.py` for imports
- `conftest.py`
- test files names starting from `test_`
- descriptive tests' names
- followed the "arrange, act, assert"