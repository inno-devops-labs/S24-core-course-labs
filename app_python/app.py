# app.py
import pytz as pytz
from flask import Flask, render_template
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import datetime


app = Flask(__name__, template_folder='templates')


grafana_metrics_counter = Counter(
    'grafana_metrics_counter',
    'metrics',
)


@app.route('/metrics')
def grafana_health_check():
    grafana_metrics_counter.inc()
    metrics = generate_latest()

    return metrics, 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route('/')
def home():
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
