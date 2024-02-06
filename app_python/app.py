"""
A simple Flask web app that displays the current time in Moscow.

This web app uses Flask to create a single route that renders an HTML template.
The current time in Moscow is calculated using the pytz library.

Requirements:
    - Flask: pip install Flask
    - pytz: pip install pytz

Usage:
    1. Save this script as 'app.py'.
    2. Create a 'templates' folder in the same directory.
    3. Save the HTML template as 'index.html' in the 'templates' folder.
    4. Run the script: python app.py
    5. Open your browser and go to http://localhost:5000 to view the Moscow time.

Note:
    Make sure to have an HTML template named 'index.html' with appropriate placeholders.

"""

from flask import Flask, render_template
from datetime import datetime, timedelta
import pytz
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)


@app.route('/')
def display_moscow_time():
    """
        Route function to display the current time in Moscow.

        Returns:
            str: Formatted string representing the current time in Moscow.

    """
    try:
        # Get the current time in UTC
        utc_now = datetime.utcnow()

        # Set the timezone to Moscow
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = utc_now.replace(tzinfo=pytz.utc).astimezone(moscow_tz)

        # Format the time as a string
        formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

        # Log the successful time retrieval
        logging.info('Moscow time retrieved successfully.')

        # Render the template with the formatted time
        return render_template('index.html', moscow_time=formatted_time)

    except Exception as e:
        # Log the error if an exception occurs
        logging.exception('An error occurred: %s', str(e))
        return 'An internal server error occurred.', 500


if __name__ == '__main__':
    app.run(debug=True)
