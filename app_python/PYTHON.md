# Python web application

## Justification of 'Flask' framework choice

Flask is a suitable choice for a simple web app displaying the current time in Moscow due to the following reasons:

### Simplicity
Flask is a lightweight and easy-to-use web framework that is well-suited for small projects. It doesn't come with unnecessary components, making it straightforward for a task with minimal requirements.

### Quick Setup
Flask has a simple and quick setup process. You can have a basic web app up and running with just a few lines of code, which is ideal for projects with limited scope like displaying the current time.

These lines of code are enough to run application:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

### Extensibility
While Flask is simple, it remains extensible. If your project requirements evolve and you need to add more features, Flask allows you to scale the application by incorporating additional libraries and components.

### Community Support
Flask has a strong and supportive community. If you encounter any issues or have questions during development, you can easily find resources and documentation to assist you. It is a great benefit for people, who have little experience in web application development like me.

### Template Rendering
Flask integrates well with template engines, making it convenient to separate the HTML presentation from the Python code. This is useful for maintaining clean and organized code.

In summary, Flask's simplicity, quick setup, and extensibility make it a justified choice for a small web app project, especially when the requirements are as straightforward as displaying the current time in Moscow.

## Implemented Best Practices

### Project Structure

The code is organized with a clear directory structure, including a separate `templates` folder for HTML templates.

### Use Version Control
While not explicitly shown in the provided code, version control using a tool like Git is encouraged for tracking changes.

### Logging
Logging is implemented using Python's built-in logging module. Relevant events and errors are logged to a file (`app.log`) for debugging and monitoring purposes.

### Use Templates
The code leverages Flask's template system by rendering an HTML template (`index.html`) to display the time.

### Code Comments
Code comments can improve code readability and help others understand the code's purpose and logic.

### Testing
While testing is not demonstrated in the provided code, it was done manually.

### Documentation
The code includes docstrings and comments to provide explanations for functions, classes, and any non-obvious code sections. This helps improve code readability and assists others in understanding the purpose and logic of the code. Additionally, providing instructions for setup and usage in a README file or inline comments is considered a best practice.

### Code writing standard
The code was written according to PEP8 standard. Code received 84% quality [on this service](https://www.pythonchecker.com/) 

### Git Ignore
The code includes a `.gitignore` file, it's a good practice to use one to exclude unnecessary files from version control.

# Unit Test

I've made some improvements to the application code by breaking it down into smaller units. Each unit is now tested to ensure its correctness. Currently, there are three units:

- `get_moscow_time`: retrieves the time in the Moscow timezone.
- `formatted_time`: returns a string of the date in a specified format.
- `display_moscow_time`: renders the page with the Moscow time displayed.

## Tests Description

### Time Accuracy Testing

This test is implemented in the `test_time_accuracy()` function. It verifies that the time returned by `get_moscow_time` is close to the actual time in the Europe/Moscow timezone, with an acceptable difference of up to several seconds.

### Time Format

The `test_time_format()` function handles this test. Here, we ensure that the string returned by the `formatted_time` function conforms to the expected format.

### Rendering Test

Implemented in the `test_display_moscow_time()` function, this test checks that the GET request returns the expected response.

## Best Practices Used in Testing

In developing these unit tests, I aimed to adhere to best practices inspired by [this source](https://www.simform.com/blog/unit-testing-best-practices/).

### Write Readable Tests

The script commences with clear and concise documentation, elucidating requirements, usage instructions, and noteworthy considerations. This documentation facilitates rapid comprehension and utilization of the test suite by developers.

### Avoid Magic Numbers and Magic Strings

The avoidance of magic strings or numbers enhances test readability. By eschewing these, tests become more comprehensible, steering readers away from fixating on arbitrary values and towards understanding the underlying test logic.

### Avoid Test Interdependencies

Tests are designed to check independent units of the application. Consequently, they can be executed in any order without impacting their validity. This fosters a modular and flexible testing environment.

### Write Deterministic Tests

Deterministic tests exhibit consistent behavior across multiple runs, unless the underlying code changes. This ensures that tests either consistently pass or consistently fail until addressed, facilitating reliable validation of application functionality.

### Modular Test Structure

Tests are structured into discrete functions, with each function dedicated to testing a specific component or feature of the Flask web app. This modular organization enhances code readability and maintainability, facilitating easier comprehension and modification of tests.

### Refrain from Multiple Asserts in a Single Unit Test

Each test contains only one assertion, promoting clarity and simplicity in test cases. By adhering to this practice, each test focuses on verifying a single aspect of the application's behavior, avoiding clutter and confusion.

These best practices collectively contribute to the effectiveness, reliability, and maintainability of the unit tests for the Flask web app.