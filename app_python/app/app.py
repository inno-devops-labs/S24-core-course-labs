from flask import Flask
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
load_dotenv()
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')

grafana_health_check_counter = Counter(
    'grafana_health_check_total',
    'Total number of health checks for Grafana',
)


@app.route('/')
def get_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f'The current time in Moscow is: {current_time}'


@app.route('/metrics')
def metrics():
    grafana_health_check_counter.inc()
    prometheus_metrics = generate_latest()

    return prometheus_metrics, 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
