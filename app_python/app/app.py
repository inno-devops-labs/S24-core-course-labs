"""
This is a simple python web application that shows current time in Moscow.
Author: Dmitrii Alekhin (d.alekhin@innopolis.university)
"""

from datetime import datetime, timezone, timedelta
from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, render_template


import os


HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8080"))
VISITS_FILE = os.environ.get("VISITS_FILE", "app/data/visits.txt")


def increment_visits():
    with open(VISITS_FILE, "r") as file:
        v = int(file.read())

    with open(VISITS_FILE, "w") as file:
        file.write(str(v + 1))


def create_app():
    """
    Creates an app and configures env
    """

    app = Flask(__name__)
    metrics = PrometheusMetrics(app)
    metrics.info("app_info", "Application info", version="1.0.0")

    if not os.path.isfile(VISITS_FILE):
        parent_dir = os.path.join(VISITS_FILE, os.pardir)
        os.makedirs(os.path.abspath(parent_dir), exist_ok=True)

        with open(VISITS_FILE, "w") as file:
            file.write("0")

    @app.route("/", methods=["GET"])
    def index():
        """
        Returns an html page with current time in Moscow
        """
        increment_visits()
        zone = timezone(timedelta(hours=3))
        time = datetime.now(timezone.utc).astimezone(zone)
        return render_template("index.html", time=time)

    @app.route("/visits", methods=["GET"])
    def visits():
        """
        Returns total number of visits
        """
        with open(VISITS_FILE, "r") as file:
            return {"visits": int(file.read())}

    return app


wsgi_app = create_app()


if __name__ == "__main__":
    print(os.getcwd())
    wsgi_app.run(host=HOST, port=PORT)
