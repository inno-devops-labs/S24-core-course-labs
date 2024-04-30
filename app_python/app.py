from flask import Flask, render_template
from prometheus_client import Counter, generate_latest
from prometheus_client.core import REGISTRY
import pytz
import logging
from datetime import datetime
import os

app = Flask(__name__)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total number of '
                        'requests received by application')


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


def check_visits(increment=False):
    """
    Check existance of visits file. Create if didn't find.

    args:
        increment: if True, then increment visits by 1.
    """
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/visits'):
        with open('data/visits', 'w') as f:
            f.write('0')
    if not increment:
        return
    with open('data/visits', 'r') as f:
        file_content = f.read()
        if len(file_content) == 0:
            counter = 0
        else:
            counter = int(file_content)
    with open('data/visits', 'w') as f:
        f.write(str(counter + 1))


@app.route('/')
def show_time():
    """
    Route to display the current time on the homepage.

    Returns:
        render_template: Renders the index.html template with the current time.
    """
    REQUEST_COUNT.inc()
    logger.info('Homepage accessed')
    check_visits(increment=True)
    return render_template('./index.html', time=get_time())


@app.route('/visits')
def show_visits():
    """
    Route to display the current number of visits on the homepage.

    Returns:
        render_template: Renders the visits.html template with the current
        number of visits.
    """
    check_visits()
    with open('data/visits', 'r') as f:
        counter = int(f.read())
        return render_template('./visits.html', visits=counter)


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
