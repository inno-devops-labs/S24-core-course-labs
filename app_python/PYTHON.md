## Best Practices Applied in the Web Application
## Framework Choice
FastAPI was chosen for developing the Python web application due to its high performance, asynchronous support, and automatic API documentation generation capabilities. FastAPI is well-suited for building modern, efficient web APIs.

## Code Organization
The code is organized into separate files for better readability and maintainability. The main application logic is contained within the main.py file, while the tests are kept in a separate test file.

## Dependency Management
The requirements.txt file lists all the dependencies required to run the application. This ensures that anyone cloning the repository can easily set up the environment with the necessary packages.

## Config management
The app takes the config variables from env

## Coding Standards
The code follows the PEP 8 style guide for Python code. Tools like Flake8 and Black have been integrated into the development workflow to enforce coding standards and maintain consistent code formatting.

## Testing
The application includes comprehensive unit tests using the pytest framework. These tests cover both the main functionality of the application and edge cases to ensure robustness.

## Timezone Handling
The application uses the pytz library to handle timezones accurately. This ensures that the displayed time is always correct for the specified timezone (Moscow in this case).

## Continuous Integration
The project can be integrated with continuous integration services like GitHub Actions or Travis CI to automate the testing process and ensure that new changes don't introduce regressions.