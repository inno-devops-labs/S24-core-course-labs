"""
This module defines a Flask application to display the current time in Moscow.
"""

from datetime import datetime
import pytz
from flask import Flask

app = Flask(__name__)


# Define a route to display the current time in Moscow
@app.route('/')
def display_time():
    """
    Display the current time in Moscow.
    """
    city_timezone = pytz.timezone('Europe/Moscow')
    city_time = datetime.now(city_timezone)
    formatted_city_time = city_time.strftime('%Y-%m-%d %H:%M:%S')
    return f'Current time in the city: {formatted_city_time}'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    