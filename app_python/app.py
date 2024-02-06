"""
This is a simple python web application that shows current time in Moscow.
Author: Dmitrii Alekhin (d.alekhin@innopolis.university)
"""

from datetime import datetime, timezone, timedelta
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Returns an html page with current time in Moscow
    """
    zone = timezone(timedelta(hours=3))
    time = datetime.now(timezone.utc).astimezone(zone)
    return render_template("index.html", time=time)


if __name__ == "__main__":
    app.run()
