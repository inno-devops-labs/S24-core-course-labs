import datetime
import os
from pathlib import Path
from zoneinfo import ZoneInfo
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

visits_path = Path("/data/visits")
if not os.path.isfile(visits_path):
    with open(visits_path, 'w+') as f:
        f.write("0")

def get_moscow_time():
    time_zone = ZoneInfo("Europe/Moscow")
    return datetime.datetime.now(time_zone).strftime("%H:%M:%S")

def get_visits_count():
    with open(visits_path, 'r') as f:
        try:
            return int(f.read())
        except ValueError:
            return 0

def increment_visits_count():
    current = get_visits_count()
    with open(visits_path, 'w') as f:
        f.write(str(current + 1))

@app.route("/")
def index():
    increment_visits_count()
    return get_moscow_time()

@app.get('/visits')
def get_visitors():
    return get_visits_count()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    from waitress import serve
    serve(app, port=port)