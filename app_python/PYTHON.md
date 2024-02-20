## Framework

For this lab I chose FastAPI as the framework for several reasons:

1. **_Performance:_** FastAPI is renowned for its exceptional performance.
   Also, it is built on top of Starlette and Pydantic.
2. **_Asynchronous Support:_**  FastAPI fully supports asynchronous programming, which is beneficial for I/O-bound
   operations such as network requests and database queries.
3. **_Modern Features:_** FastAPI leverages Python 3.7+ type hints and pydantic models. These features facilitate
   automatic data validation, serialization, and documentation generation.
4. **_Easy to use_**: FastAPI has a clean and intuitive syntax, making it easy to learn and use. In addition, I already
   have some experience using this framework.

## Best practices

- **_Error Handling:_** Error handling in the application is implemented so it can catch exceptions.
- **_PEP 8 Compliance:_** The code follows the PEP 8 style guide for Python code.
- **_Manual Testing:_** I manually tested the application on my local machine.

## Unit Tests

I have created unit tests for the FastAPI application using the _**pytest**_ framework. The tests cover various
scenarios to ensure the correctness and robustness of the application.

- `test_msc_time_root`:  
  This test verifies that the root endpoint ("/") returns a valid response with a status code of 200,
  content type of HTML, and includes the current time in the response body.

- `test_msc_timezone`:  
  This test checks if providing an invalid timezone in the request header results in an error.

- `test_msc_time_invalid_path`:  
  This test ensures that accessing an invalid path returns a 404 response.

- `test_msc_time_post`:  
  This test ensures that app returns a 405 response when post request is made.

### Best Practices

- **_Modularity_**:  
  Each test case is isolated and focuses on testing a specific aspect of the application.

- **_Assertions_**:  
  Assertions are used to validate the expected behavior of the application.

- **_Parametrization_**:  
  Where applicable, parametrization is used to test multiple scenarios with different inputs, maximizing
  test coverage.