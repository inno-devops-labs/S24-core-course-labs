"""
Main application file. Contains the route information and necessary setups.
"""

import os

from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

from app_python.app_utils import increment_visits, return_time, return_visit_counts

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@metrics.counter(
    "requests_by_endpoint",
    "Number of requests by endpoint",
    labels={"endpoint": lambda: request.endpoint},
)
@app.route("/")
def show_time():
    """
    Index page. Shows the current time in Moscow.
    """
    increment_visits()
    timezone = os.getenv("APP_TIMEZONE", "Europe/Moscow")
    return return_time(timezone)


@app.route("/metrics")
def show_prometheus_metrics():
    """
    Metrics page. Shows the current time in Moscow in Prometheus format.
    """
    return return_time("Europe/Moscow", prometheus=True)


@app.route("/visits")
def show_visits():
    """
    Visits page. Shows the number of visits to the page.
    """
    return return_visit_counts()
