from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)
metrics = PrometheusMetrics(app)
timezone = ZoneInfo('Europe/Moscow')

metrics.info('app_info', 'Python Web Application', version='1.8')


@app.route("/")
def index():
    return f"Current time in Moscow: {current_time()}"


def current_time():
    return datetime.now(timezone).time().isoformat('seconds')
