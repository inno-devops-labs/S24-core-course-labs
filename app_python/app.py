"""
A simple web application that displays the current time in Moscow.
"""

import datetime
from flask import Flask, render_template
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the home page that displays the current time in Moscow.
    """
    moscow_time = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=3)))
    return render_template('index.html', time=moscow_time)


@app.route('/metrics')
def metrics():
    """
    Returns the metrics from registry as text string.
    """
    return generate_latest()


if __name__ == '__main__':
    app.run()
