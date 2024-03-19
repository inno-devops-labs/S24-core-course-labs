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
    5. Open browser and go to http://localhost:5000 to view the Moscow time.

Note:
    Make sure to have an HTML template named 'index.html' with appropriate
     placeholders.

"""

from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


def get_moscow_time():
    """
    Function to find the current time in Moscow.

    Returns:
        datetime: Current time in Moscow.

    """
    # Get the current time in UTC
    utc_now = datetime.utcnow()

    # Set the timezone to Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = utc_now.replace(tzinfo=pytz.utc).astimezone(moscow_tz)

    return moscow_time


def formatted_time(time):
    """
    Function to format the given time.

    Args:
        time (datetime): Time to be formatted.

    Returns:
        str: Formatted time string.

    """
    return time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def display_moscow_time():
    """
        Route function to display the current time in Moscow.

        Returns:
            str: Formatted string representing the current time in Moscow.

    """
    time = formatted_time(get_moscow_time())

    # Render the template with the formatted time
    return render_template('index.html', moscow_time=time)


if __name__ == '__main__':
    app.run(debug=True)