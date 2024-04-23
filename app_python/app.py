"""
A simple web application that displays the current time in Moscow.
"""

import datetime
from flask import Flask, render_template
from prometheus_client import generate_latest

app = Flask(__name__)
visits_file_path = "visits_cnt.txt"
try:
    visits_cnt = int(open(visits_file_path, "w+").read())
except ValueError:
    visits_cnt = 0


@app.route('/')
def home():
    """
    Renders the home page that displays the current time in Moscow.
    """
    global visits_cnt

    visits_cnt += 1
    with open(visits_file_path, "w+") as f:
        f.write(str(visits_cnt))

    moscow_time = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=3)))
    return render_template('index.html', time=moscow_time)


@app.route('/metrics')
def metrics():
    """
    Returns the metrics from registry as text string.
    """
    return generate_latest()


@app.route("/visits")
def visits():
    """
    Returns number of visits of the main page
    """
    return str(visits_cnt)


if __name__ == '__main__':
    app.run()
