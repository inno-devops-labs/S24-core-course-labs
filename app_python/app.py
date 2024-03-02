"""
This is a simple python web application that shows current time in Moscow.
Author: Dmitrii Alekhin (d.alekhin@innopolis.university)
"""

from datetime import datetime, timezone, timedelta
from os import environ
from flask import Flask, render_template


HOST = environ.get("HOST", "0.0.0.0")
PORT = int(environ.get("PORT", "8080"))


def create_app() -> Flask:
    """
    Creates an application and configures routes
    """
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        """
        Returns an html page with current time in Moscow
        """
        zone = timezone(timedelta(hours=3))
        time = datetime.now(timezone.utc).astimezone(zone)
        return render_template("index.html", time=time)

    return app


wsgi_app = create_app()


if __name__ == "__main__":
    wsgi_app.run(host=HOST, port=PORT, debug=False)