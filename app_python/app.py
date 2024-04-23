"""A Python web application to display the current time in Moscow."""

from datetime import datetime, timezone, timedelta
from flask import Flask, render_template, Response
from prometheus_client import start_http_server, Summary, Counter
import prometheus_client

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
VISIT_COUNTER = Counter('visits_total', 'Total number of visits')

visit_count = 0

app = Flask(__name__)

@app.route('/visits')
def visits():
    global visit_count
    return f'Total visits: {visit_count}'

try:
    with open('data/visits.txt', 'r') as f:
        visit_count = int(f.read())
except FileNotFoundError:
    visit_count = 0

def save_visit_count(count):
    with open('data/visits.txt', 'w') as f:
        f.write(str(count))

def get_moscow_time():
    """Get the current time in Moscow."""
    moscow_timezone = timezone(timedelta(hours=3))
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
@REQUEST_TIME.time()
def index():
    """Render the index page with the current time in Moscow."""
    global visit_count
    visit_count += 1
    save_visit_count(visit_count)
    moscow_time = get_moscow_time()
    return render_template('index.html', time=moscow_time)

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
