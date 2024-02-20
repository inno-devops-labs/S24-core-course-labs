"""
A simple web application that displays the current time in Moscow.
"""

import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the home page that displays the current time in Moscow.
    """
    moscow_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    return render_template('index.html', time=moscow_time)


if __name__ == '__main__':
    app.run()
