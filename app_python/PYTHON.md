# Moscow timezone time web application

The document provide brief explanation of best practices applied in python application developing. It explains such topics as coding standards, "hand" testing, and ensuring code quality.

## Flask usability

`Flask` framework was used because:

- it is support extensions which can be applied in app in future;
- huge amount of documentation and user experience - easy to use and find information;
- it is very simple to understand and run application;
- I just want to learn something new.

### Best practices applied

- To ensure code quality `autopep8` was used as a formatter which is follows `PEP8` standarts;
- The application was tested by hands. It displays the correct time in correct format updates upon page refreshing;
- To avoid conflict in global environment all dependencies were installed using venv (virtual environment);
- Only proper libraries was used to develop this app to avoid displaying incorrect format of time.

## Unit Tests 

To ensure correctness of the code unit tests also was implemented.
- `test_get_moscow_time_format` tests that the time which was taken from library comes in appropiate format %H:%M:%S;
- `test_msk_timezone` tests that current time which is taken from library is bigger than time from function msk_time.

### Best practices applied to unit tests

- AAA practice was used during writing unit tests for the app;
- Only one scenario was tested during the test;
- Unit tests are also automated by CI workflow;
- Two tests was devided into functions to test the app independetly.
