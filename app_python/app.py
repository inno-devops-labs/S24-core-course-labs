"""
Web application that shows current time in Moscow
"""
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, redirect, render_template, Response
from prometheus_client import generate_latest


app = Flask(__name__)
visits_file = "./data/visits.txt"


@app.route("/")
def index():
    """
    Index page. Redirects to /show_moscow_time
    """
    return redirect("/show_moscow_time")


def increment_visits():
    """
    Increment number of visits and write to file
    """
    if not os.path.exists(visits_file):
        os.mkdir(os.path.dirname(visits_file))
        with open(visits_file, "w", encoding="utf-8") as f:
            f.write("0")

    with open(visits_file, "r+", encoding="utf-8") as f:
        visits_cnt = str(int(f.read()) + 1)
        f.seek(0)
        f.write(visits_cnt)


@app.route("/show_moscow_time")
def show_moscow_time():
    """
    Shows current time in Moscow
    """
    increment_visits()

    current_time = datetime.now(tz=ZoneInfo("Europe/Moscow"))

    return render_template('moscow_time.html', title="Current time in Moscow",
                           current_time=current_time)


@app.route("/metrics")
def metrics():
    """
    Returns Prometheus metrics
    """
    return Response(generate_latest(), mimetype='text/plain')


@app.route("/visits")
def visits():
    """
    Returns number of visits
    """
    with open(visits_file, "r", encoding="utf-8") as f:
        return {'visits': int(f.read())}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
