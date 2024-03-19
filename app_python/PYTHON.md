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
