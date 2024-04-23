"""Web app for showing current time in Moscow"""

from prometheus_flask_exporter import PrometheusMetrics

import os
import threading

from datetime import datetime
from flask import Flask
import pytz


PORT = 5000
app = Flask(__name__)
visits = 0
visits_store_path = "data/visits"
visits_lock = threading.Lock()

# Initialize PrometheusMetrics for the app
metrics = PrometheusMetrics(app)


def save_visits():
    if not os.path.exists("data"):
        os.mkdir("data")
    with open(visits_store_path, "w") as file:
        file.write(str(visits))


def inc_visits():
    global visits
    visits_lock.acquire()
    visits += 1
    visits_lock.release()
    save_visits()


@app.route('/')
def index():
    """Returns current time in Europe/Moscow timezone"""
    inc_visits()
    tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"The current time in Moscow is {moscow_time}"


@app.route('/time')
def get_current_time():
    inc_visits()
    """Return current time in Europe/Moscow timezone in json format"""
    tz = pytz.timezone('Europe/Moscow')
    return {"time": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")}


@app.route('/visits')
def get_visit_count():
    """Returns number of visits of site"""
    inc_visits()
    with open(visits_store_path, "r") as file:
        return {"visits": int(file.read())}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
    save_visits()
