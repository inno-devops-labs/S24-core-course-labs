"""
Web application that shows current time in Moscow
"""
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, redirect, render_template, Response
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route("/")
def index():
    """
    Index page. Redirects to /show_moscow_time
    """
    return redirect("/show_moscow_time")


@app.route("/show_moscow_time")
def show_moscow_time():
    """
    Shows current time in Moscow
    """
    current_time = datetime.now(tz=ZoneInfo("Europe/Moscow"))

    return render_template('moscow_time.html', title="Current time in Moscow",
                           current_time=current_time)


@app.route("/metrics")
def metrics():
    """
    Returns Prometheus metrics
    """
    return Response(generate_latest(), mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
