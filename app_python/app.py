"""
Main application file. Contains the route information and necessary setups.
"""

from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

from app_python.app_utils import return_time

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@metrics.counter("requests_by_endpoint", "Number of requests by endpoint", labels={"endpoint": lambda: request.endpoint})
@app.route("/")
def show_time():
    """
    Index page. Shows the current time in Moscow.
    """
    return return_time("Europe/Moscow")

@app.route("/metrics")
def show_prometheus_metrics():
    """
    Metrics page. Shows the current time in Moscow in Prometheus format.
    """
    return return_time("Europe/Moscow", prometheus=True)