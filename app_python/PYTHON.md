## Justification for Choosing Flask

Flask is a micro-framework for Python that is lightweight and easy to use. It is well-suited for small to medium-sized projects, making it an excellent choice for this simple web application. Here are a few reasons why Flask was chosen:

1. **Simplicity:** Flask follows the "micro" philosophy, providing the essentials to get a web application up and running without unnecessary features. This simplicity is beneficial for a small project like displaying the current time.

2. **Ease of Use:** Flask has a straightforward API and minimal boilerplate code, making it easy for developers to understand and work with. This is especially advantageous for beginners and quick development tasks.

3. **Flexibility:** While being lightweight, Flask allows developers to choose their preferred libraries for various components, providing flexibility in terms of database, templating, and more.

4. **Community Support:** Flask has a vibrant and active community, which means extensive documentation, a plethora of tutorials, and a wide range of extensions available for additional functionality.

5. **Testing:** Flask provides a built-in development server that supports quick testing. Additionally, it integrates well with testing libraries, making it convenient to implement test-driven development.

Overall, Flask strikes a balance between simplicity and functionality, making it an ideal choice for a small web application like displaying the current time in Moscow.

# Best Practices in Web Application

## Coding Standards
1. **PEP 8 Compliance:** The code follows the PEP 8 style guide for Python, ensuring consistency and readability.
2. **Descriptive Naming:** Meaningful variable and function names are used throughout the codebase, enhancing clarity and maintainability.
3. **Unit Testing:** ```Pytest``` is used to test the application with unt testing.
4. **Linting:** ```Flake8``` is used to identify and address potential code issues and maintain consistency.
5. **Dependency management:** requirements.txt file lists all the dependencies required to run the application. This ensures that anyone cloning the repository can easily set up the environment with the necessary packages.
6. **Documentation:** Code is adequately documented using docstrings and inline comments, providing insights into functionality and usage.