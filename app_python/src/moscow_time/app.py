from flask import Flask, Response
from datetime import datetime
import pytz
from prometheus_client import generate_latest, Counter


app = Flask(__name__)

healthcheck_counter = Counter(
    'healthcheck_requests',
    'Number of healthcheck requests'
)

@app.route('/')
def display_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f'The current time in Moscow is: {current_time}'

@app.route('/healthcheck')
def healthcheck():
    healthcheck_counter.inc()
    return 'Ok'


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
