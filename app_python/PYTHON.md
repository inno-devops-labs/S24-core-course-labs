# Python Web Application

## Rationale for the web framework

I chose the `aiohttp` web framework for these reasons:

- It is a popular and well-maintained web framework;
- It is built upon async Python;
- It is simple and light-weight, compared to frameworks such as Django.

## Best practices

In my web app, I used these best practices:

- I created a virtual environment to isolate installed packages for my app;
- I used type annotations to ensure that the code is correct.

In addition, I formatted my code using `black` and ran `pylint` to find any
potential problem in my code.

## Testing

The application is quite small, and `get_current_time` is the only
function one can write unit tests for (other tests would be integration tests).
For `get_current_time`, I test these properties:

- The returned time is not too old;
- The timezone is correct;
- The returned time is monotonic.

While writing tests, I followed these best practices:

- Write tightly scoped unit tests;
- Check that the tests work by intentionally introducing a bug.
