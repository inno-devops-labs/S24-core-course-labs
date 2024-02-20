# Python Web Application Best Practices

## Coding Standards and Best Practices

### 1. Code Organization

- The project follows a modular structure to enhance maintainability.
- Each component, such as routes, templates, and static files, is organized into separate directories.
- As for the naming convention, 'lower_with_under' and 4 spaces as indentation has used.  
### 2. PEP 8 Compliance

- The Python code adheres to PEP 8 coding standards for readability and consistency. VS Code has been used.

### 3. Comments and Documentation

- Code is well-documented with inline comments for complex sections and function docstrings for clarity.
- External documentation is maintained for project setup, dependencies, and usage.

### 4. Version Control

- A clean `.gitignore` file is used to exclude unnecessary files and directories from version control.
- Descriptive commit messages are employed for better tracking and collaboration.

## Testing

There are no automated tests, however it is assured that program is working via manual testing.

## README.md in app_python Folder

Proper readme file has provided with all information needed.

### Project Overview

Provide a brief overview of the Python web application, its purpose, and features.
This app developed on Python3 and html. We used Flask framework as our web application. Its purpose is showing the time in Moscow, Russia. It is not dependent on the devices' timezone, It always shows the Moscow time and update itself automatically every second. For more readibility we used styling. 
 
### Installation
Download the folder, then run python file by 
```bash
python3 app.py
```
Then you can open the website by entering http://127.0.0.1:5000

## Unit Tests

We've implemented comprehensive unit tests for the Flask application using the `unittest` framework. The tests ensure that the application behaves correctly under different circumstances.

### Test Coverage

1. **test_index_route**: This test ensures that the index route (`'/'`) returns a status code of 200 (OK).
2. **test_index_content**: This test verifies that the index route (`'/'`) contains the expected content "Moscow Time".
3. **test_title_content**: This test checks if the title tag with the text "Moscow Time Digital Clock" is present in the HTML response.
4. **test_clock_script**: This test verifies if the script tag containing the JavaScript function `updateClock()` is present in the HTML response.

### Running the Tests

To run the unit tests, execute the `test_app.py` file:

```bash
python test_app.py
```
### Best Practices Applied
1. **Separation of Concerns**: The application logic is separated from the test logic, following the principle of separation of concerns.
2. **Use of Test Client**: We utilize Flask's test client to simulate requests to our application, enabling us to test our routes and responses efficiently.
3. **Readable Test Methods**: Test methods are named descriptively, making it clear what aspect of the application functionality they are testing.