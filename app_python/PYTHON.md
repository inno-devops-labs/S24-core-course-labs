# Best practices & Framework choice

- This app is written using Flask framework because it is easy and convenient. The project is not hard, that is why Flask was chosen.
- Coding standards & Code quality
  - The code follows style conventions in PEP 8. The code was verified using `pycodestyle 2.11.1` tool.
  - You can check it by yourself: `pycodestyle --first ./app.py`
  - The code is formatted using Black (Python code formatter).

# Testing

## Unit tests
- Test **test_status_code** verifies that the base route returns a correct status code 200.
- Test **test_time** verifies that the displayed time on the base page returns correct Moscow time. It compares the expected Moscow time with an actual output on the page.

## Best practices
- Every test is isolated from one another. It means that a test does not depend on another's state.
- Every test has a meaningful name which indicates the essense of the test. It is clear for any developer what every test serves for.
- The **setUp** method is used to configure and start testing procedure.
- Appropriate assertion functions are used (**self.assertEqual**, **self.assertIn**).

