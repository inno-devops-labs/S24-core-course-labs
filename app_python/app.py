from flask import Flask, render_template, request
from prometheus_client import Counter, generate_latest
from prometheus_client.core import REGISTRY
import pytz
import logging
from datetime import datetime

app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests received by the application')

def get_time():
    """
    Get the current time in the Europe/Moscow time zone.

    Returns:
        str: Current time formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    # Get the current time in Moscow
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    # Convert time to string
    str_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return str_time

@app.route('/')
def show_time():
    """
    Route to display the current time on the homepage.

    Returns:
        render_template: Renders the index.html template with the current time.
    """
    REQUEST_COUNT.inc()
    logger.info('Homepage accessed')
    return render_template('./index.html', time=get_time())

@app.route('/metrics')
def metrics():
    """
    Endpoint to expose Prometheus metrics.

    Returns:
        str: Prometheus-formatted metrics.
    """
    return generate_latest(REGISTRY)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
