# Python Web App

This Python web application is built to display the current time in Moscow. 

## Reasons for Using the Flask Framework

The application is developed using the Flask web framework. The choice of Flask is justified by its simplicity, lightweight nature, and suitability for small to medium-sized applications. Flask allows for quick development while providing the necessary tools for building a web application.

## Features

- Displays the current time in Moscow on the homepage.
- Utilizes the `pytz` library to handle time zones.
- Implements a simple test to ensure the displayed time adheres to the expected format.
- Follows best practices in code organization and adheres to coding standards.

## Code Structure

The code is organized into the following components:

- **app.py**: Contains the main Flask application code, including the `get_time` function to fetch the current time in Moscow and the `show_time` route to render the time on the homepage.

- **tests/test_app.py**: Implements a unit test for checking the format of the time returned by the `get_time` function.

## Best Practices Applied

### Code Organization

- The code follows the separation of concerns principle, with clear separation between the Flask application code and the testing code.
  
### Time Zone Handling

- The application uses the `pytz` library to handle time zones, ensuring accurate and reliable time information.

### Testing

- A simple unit tests are implemented in the `tests/test_app.py` file. 
- -  the correct format of the displayed time.
- The accuracy of the time values was verified by refreshing the webpage multiple times with varying delays. The test was successful.

## Testing

To run the tests, execute the following command:

```bash
python -m unittest tests.test_app.py
```

This command will verify that the time format follow to the expected 'YYYY-MM-DD HH:MM:SS' format and that the time precision is less than 1 second.

## Running the Application
To run the application locally, use the following command:
```bash
python app.py
```
Visit http://127.0.0.1:8000 in your web browser to see the current time in Moscow.
