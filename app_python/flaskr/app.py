from flask import Flask, render_template, Response
import pytz
from datetime import datetime
from prometheus_client import Counter, Gauge, Histogram
import prometheus_client
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP Requests',
    ['method', 'endpoint'])

REQUEST_DURATION = Histogram(
    'http_request_duration_seconds',
    'HTTP Request Duration',
    ['method', 'endpoint'])

ACTIVE_USERS = Gauge('active_users', 'Number of Active Users')


@app.route('/')
def index():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    start_time = time.time()
    # get time in Moscow time zone
    msk_time = datetime.now(pytz.timezone(
        'Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    REQUEST_DURATION.labels(method='GET', endpoint='/').observe(
        time.time() - start_time)
    return render_template('index.html', msk_time=msk_time)


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype='text/plain')


@app.route('/health')
def health_check():
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=False)
