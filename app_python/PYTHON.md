# Python web app

### Justification

I decided to use FastAPI, since it is popular, have good documentation and pretty easy to start with.

### Best practices

* Code Formatting and Simplicity
* Requirements specification in a requirements.txtfile

## Unit tests

### Description

1. `test_read_root` checks the `/current_time` endpoint. It sends an HTTP get request and asserts that the
response status code is 200, indicating a successful request. Then, it asserts that the returned datetime string from
the server is the same format as the current Moscow time format it generated.

2. `test_root_path` sends a get request to the root path ("/") and checks if the request is successful by
asserting the response status code to be 200. It also checks if the returned file is an HTML file by inspecting the
content-type in the response headers.

### Best practices

1. Each test is focused on one functionality

2. Assert Actual vs Expected

3. Clean, targeted testing
