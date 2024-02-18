"""
Flask Application Module

This module contains the main Flask application for the project. It defines routes and handles
the application's behavior.

Author: Herman Dyudin
"""

from datetime import datetime, timezone, timedelta
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display_time():
    """
        Display Time Route
        This route displays the current time in Moscow. It calculates the current time in UTC,
        adjusts it to the Moscow timezone, and renders a template with the formatted time.

        Returns:
            str: Formatted string representing the current time.

        Author: Herman Dyudin
        """
    moscow_time = datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=3)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('page.html', time=formatted_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
