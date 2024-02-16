# Current Moscow time web application

## Why to use Flask for web applications

I used `Flask` framework for this task because:

* it is highly scalable which is perfect for creating a web application step by step;
* it has a clear documentation and therefore easy to use;
* it has a massive user base among the tech community;
* it is lightweight and flexible.

### Best practices applied to the code

* The code is formatted using `autopep8` formatter and is following `PEP8` standards;
* all dependencies are installed using `venv` to avoid installation of Python packages globally;
* the application is tested to ensure that displayed time updates upon page refreshing.

### Unit Tests

Unit tests for this application were implemented by using `unittest` framework to ensure the correctness of the
application's functionality.

#### Tests description

* `test_response` method: This method tests whether the application responds successfully when a
  request is made
* `test_time_format` method: This method verifies whether the format of the time returned by the application
  matches the expected format for the current time in Moscow.

#### Best practices applied to unit tests

1. Isolation of Tests: Each test method focuses on testing a specific aspect of the application's functionality.
2. Descriptive Test Method Names: Test method names are descriptive and clearly indicate what aspect of the application
   they are testing.
3. Use of Standard Libraries: Utilizing standard libraries such as `unittest`, `datetime`, and `pytz` for testing and
   working with date-time operations ensures reliability and compatibility across different environments.
4. Test Setup: The setUp method is used to set up the necessary environment for each test case, ensuring consistency and
   avoiding code duplication.
