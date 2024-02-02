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


@app.route('/')
def show_time():
    """Function that returns template that renders template with current time in Moscow"""
    try:
        timezone = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
        logging.info("Template rendered with time: %s", moscow_time)
        return render_template('index.html', time=moscow_time)
    except BaseException as exception:
        logging.error("Exception %s", exception)
        return render_template("exception.html")


if __name__ == '__main__':
    app.run(debug=True)
