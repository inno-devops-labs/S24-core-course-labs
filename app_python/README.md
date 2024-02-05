# Flask MSK Timezone Web Application

## Introduction

This Flask application provides a simple web service to display the current time in the Moscow (MSK) timezone. It utilizes the Flask micro-framework for Python and the pytz library for timezone handling.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd app-python
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python3 app.py
   ```

2. Access the web service:

   Navigate to `http://127.0.0.1:5000/msk_timezone` in your web browser. You should see the current time in the Moscow timezone displayed.

## File Structure

- `app.py`: Contains the main Flask application code, including the route for fetching the current time in the Moscow timezone.
- `requirements.txt`: Lists the required Python packages and their versions for running the application.
- `PYTHON.md`: Justifies the choice of Flask framework and describes best practices applied in the web application, including coding standards, testing, and code quality.

## Additional Information

- **Flask Version**: 3.0.2
- **pytz Version**: 2024.1
