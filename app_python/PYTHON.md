# Justification for Choosing FastAPI

- **High Performance**: FastAPI provides high performance due to its asynchronous support, making it one of the fastest web frameworks in the Python ecosystem.
- **Ease of Use**: Offers an intuitive design and automatic documentation generation, streamlining development and debugging processes.
- **Asynchronous Support**: Its built-in support for asynchronous request handling allows for efficient handling of numerous simultaneous connections.
- **Automatic Data Validation**: Uses Pydantic for automatic data validation, easing the parsing and validation of complex data and structures.
- **Developer Productivity**: Features like automatic API documentation (with Swagger UI and ReDoc) enhance developer productivity and facilitate a better development experience.
- **Strong Community and Documentation**: A growing community and comprehensive documentation aid in quick problem-solving and learning.

Choosing FastAPI leverages these advantages, ensuring the web application is efficient, maintainable, and scalable, while remaining within the Python ecosystem.

# Best Practices in FastAPI Web Application Development

## Best Practices Applied

- **Virtual Environments**: Utilized virtual environments to manage dependencies, ensuring that the application runs reliably in any deployment environment.
- **Dependency Management**: Maintained a concise `requirements.txt` file, listing all necessary dependencies explicitly to ensure reproducibility.
- **Testing**: Wrote automated test to make sure of the website is functioning as expected.
- **PEP 8 Compliance**: Followed PEP 8 guidelines for Python code style to maintain readability and consistency across the codebase.
- **Type Annotations**: Used type annotations to improve code clarity and facilitate error detection at development time.
- **Docstrings**: Documented functions and classes using docstrings, providing clear explanations of their purpose and usage.


# Testing

Testing is an integral part of developing a robust web application with FastAPI. It ensures that the application behaves as expected under various scenarios and maintains high-quality standards over time. Below, we describe the unit tests created for our FastAPI application and the best practices applied during the testing process.

## Unit Tests

### Test for Time Updates

**Objective:** To verify that the time displayed on the web application updates correctly at least every 5 seconds.

**Method:**
- The test sends an initial GET request to the application's root endpoint and captures the time displayed on the page.
- It then pauses execution for 5 seconds before sending a second GET request to the same endpoint.
- The test asserts that the time captured from the second request is different from the first, ensuring that the time updates as expected.

**Best Practices Applied:**
- **Automated Testing**: This test is automated, making it possible to repeatedly verify the application's behavior with minimal effort.
- **Real-World Scenario Simulation**: By waiting 5 seconds between requests, the test simulates a real-user scenario, enhancing the test's relevance.

### Test for Time Format

**Objective:** To ensure that the time displayed on the web application adheres to the correct format (HH:MM:SS).

**Method:**
- A GET request is made to the application's root endpoint, and the time displayed on the page is captured.
- The test uses a regular expression to validate that the captured time matches the expected format.
- It asserts that the time string conforms to the HH:MM:SS format, indicating correct time representation.

**Best Practices Applied:**
- **Precision in Testing**: By using a regular expression for format validation, the test precisely verifies the format of the time string, ensuring accuracy in the application's output.
- **Logging**: The test logs the time obtained during testing, providing useful information for debugging purposes in case of test failure.

## Best Practices in Testing

In developing these tests, several best practices were adhered to, enhancing the quality and reliability of the testing process:

- **Isolation of Test Cases**: Each test focuses on a single functionality, ensuring test clarity and making it easier to identify issues.
- **Use of Assertions**: Assertions are used to compare the expected outcomes with actual outcomes, providing a clear pass/fail result for each test.
- **Automated Testing**: Automating the tests allows for easy repetition and integration into a continuous integration/continuous deployment (CI/CD) pipeline, ensuring that tests are run consistently.
- **Test Coverage**: By covering different aspects of the application's functionality, such as time updates and format correctness, we ensure a comprehensive evaluation of the application's behavior.
