"""Web app for showing current time in Moscow"""

from prometheus_flask_exporter import PrometheusMetrics

from datetime import datetime
from flask import Flask
import pytz


PORT = 5000
app = Flask(__name__)

# Initialize PrometheusMetrics for the app
metrics = PrometheusMetrics(app)


@app.route('/')
def index():
    """Returns current time in Europe/Moscow timezone"""
    tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"The current time in Moscow is {moscow_time}"


@app.route('/time')
def get_current_time():
    """Return current time in Europe/Moscow timezone in json format"""
    tz = pytz.timezone('Europe/Moscow')
    return {"time": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
