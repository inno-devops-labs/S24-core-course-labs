## Which best practices were applied?
    
* Explicit relative imports: The script uses explicit relative imports to bring in the modules it needs. 

* Use of \__name__ guard: The script uses the \__name__ == '\__main__' guard to ensure that certain parts of the code are only run when the script is executed directly, and not when it's imported as a module.

* Function definition: The function call_time() is defined clearly and its purpose is evident. This is in line with the best practice of writing functions that perform a single task and are named accordingly.

* Code follows PEP 8 style guide.

* Сode has been tested locally (pressed F5 several times :grin:)

### Some basic unit tests were added and the following best practices were followed:

* Setting up a test client: The app.test_client() is used to simulate requests to the application without running the server. This is a common practice for testing Flask applications.

* Using assertions to check response: The assert statements are used to verify that the response from the server is as expected. This is a fundamental part of any test.

* Testing for different HTTP status codes: The tests are checking for specific HTTP status codes (200 and 404) to ensure that the application behaves correctly for valid and invalid routes.

* Using regular expressions: The re.match function is used to check that the response data matches a specific pattern, which is a good way to validate the format of the response.
