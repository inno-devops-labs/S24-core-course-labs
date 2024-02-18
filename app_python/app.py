"""
Web application that shows current time in Moscow
"""
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, redirect, render_template

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


if __name__ == "__main__":
    app.run()
