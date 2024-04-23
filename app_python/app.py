from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)
metrics = PrometheusMetrics(app)
timezone = ZoneInfo('Europe/Moscow')

metrics.info('app_info', 'Python Web Application', version='1.8')

with open("visits", "r") as f:
    visit_count = int(f.readline())


@app.route("/")
def index():
    count_visit()
    return f"Current time in Moscow: {current_time()}"


@app.route("/visits")
def display_visits():
    count_visit()
    return f"Visit count: {visit_count}"


def current_time():
    return datetime.now(timezone).time().isoformat('seconds')


def count_visit():
    global visit_count
    visit_count += 1
    with open("visits", "w") as f:
        f.write(str(visit_count))
