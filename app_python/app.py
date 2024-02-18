"""Module that runs python flask application that shows current time in Moscow"""

from datetime import datetime
import logging
from flask import Flask, render_template
import pytz

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    filename="record.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)


def current_moscow_time():
    """returns current time in Moscow, Russia"""
    timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    return moscow_time


@app.route('/')
def show_time():
    """Function that returns template that renders template with current time in Moscow"""
    try:
        moscow_time = current_moscow_time()
        logging.info("Template rendered with time: %s", moscow_time)
        return render_template('index.html', time=moscow_time)
    except BaseException as exception:
        logging.error("Exception %s", exception)
        return render_template("exception.html")


@app.route('/health')
def health_check():
    """Returns ok, used as check for availability"""
    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
