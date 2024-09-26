# Lab 1

## Framework

I use FastAPI framework, because of:

- **Simplicity:** FastAPI is easy to learn and use. It has a clear and straightforward design.
- **Performance:** FastAPI is built with high-performance libraries such as Uvicorn and Pydantic.
- **Validation.** FastAPI  is optimized with Python type hint and has some automatic features like data validation and serialization.
- **Scalability:** FastAPI is built on top of Asynchronous Server Gateway Interface, so it can be used to build scalable applications and handle concurrent requests efficiently.

## Best practices:

- code following the PEP8 standards
- clear and structured architecture: `templates` folder for html files, `tests` folder for unit-tests and `static` folder for styles
- `requirements.txt` file to gather all needed for this app python packages

## Code quality

- **Flake8** as a python code linter. It’s one of the better linters that has very low false positive rate. It checks code against PEP8 style, programming errors and cyclomatic complexity.
- **Black** as a python code formatter. It's a popular auto-formatter that reformats entire files in place, applying its own PEP8-compliant coding style.
- **Mdformat** as a Markdown formatter.

## Testing

I used Python unittest library and I tried to write the testcases that cover all the requested features of the application:

- We can access the application
- The application displays the correct time
- Time is changing after refreshing the website
