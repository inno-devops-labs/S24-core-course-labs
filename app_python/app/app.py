"""
This is a simple python web application that shows current time in Moscow.
Author: Dmitrii Alekhin (d.alekhin@innopolis.university)
"""

from datetime import datetime, timezone, timedelta
from prometheus_flask_exporter import PrometheusMetrics
from os import environ
from flask import Flask, render_template


HOST = environ.get("HOST", "0.0.0.0")
PORT = int(environ.get("PORT", "8080"))


wsgi_app = Flask(__name__)
metrics = PrometheusMetrics(wsgi_app)
metrics.info("app_info", "Application info", version="1.0.0")


@wsgi_app.route("/", methods=["GET"])
def index():
    """
    Returns an html page with current time in Moscow
    """
    zone = timezone(timedelta(hours=3))
    time = datetime.now(timezone.utc).astimezone(zone)
    return render_template("index.html", time=time)


if __name__ == "__main__":
    wsgi_app.run(host=HOST, port=PORT)
