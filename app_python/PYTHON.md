# Lab 1: Web Application Development

### Best practices, applied in application:

1. The application follows a standard Flask structure with a clear separation of concerns, separating the application logic `app.py` from the presentation layer `templates/index.html`
2. Followed PEP8 standards for clean and readable code, use PyCharm linter to check errors and warnings in the code
3. Maintained a **`requirements.txt`** file listing all necessary libraries for the application
4. Created virtual environment for convenient work with dependencies

### Unit Tests:
1. test_get_current_time_format:
- Description: This test ensures that the get_current_time function returns a string in the format 'HH:MM:SS'.
- Test Strategy:
  - It checks if the returned value is a string.
  - It verifies that the returned string contains three parts separated by colons, representing hours, minutes, and seconds.
- Reasoning: This test verifies the basic behavior of the function, ensuring that it produces output in the expected format.
### Best Practices Applied to Tests:
1. Isolated Tests:
- Each test case is isolated, focusing on testing a specific aspect of the get_current_time function.
- Reasoning: Isolated tests are easier to understand, maintain, and debug.
2. Meaningful Test Names:
- Test names clearly describe the behavior being tested, such as test_get_current_time_format.
- Reasoning: Meaningful test names improve readability and provide clarity about the purpose of each test.
3. Focused Test Coverage:
- The test suite focuses on testing the format of the time returned by the get_current_time function.
- Reasoning: Focusing on specific functionality ensures that tests are concise and targeted, avoiding unnecessary complexity.
4. Readability:
- The test code is structured and formatted in a readable manner.
- Reasoning: Readable test code is easier to understand for both developers and maintainers, enhancing collaboration and code review processes.