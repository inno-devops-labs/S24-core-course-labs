from flask import Flask, render_template, Response
from datetime import datetime, timezone
import pytz
import prometheus_client

app = Flask(__name__)

VISITS_PATH = "data/visits.txt"

REQUEST_TIME = prometheus_client.Histogram('py_request_handle_time', 'Time to process a request')

def load_visits():
    try:
        with open(VISITS_PATH, 'r') as f:
            visits = int(f.readline())
    except FileNotFoundError:
        visits = 0
    return visits

def increment_visits():
    with open(VISITS_PATH, "r") as visits_file:
        try:
            visits = int(visits_file.readline())
            visits += 1
        except ValueError:
            visits = 0
            
    with open(VISITS_PATH, "w") as visits_file:
        visits_file.write(str(visits))

@app.route('/')
@REQUEST_TIME.time()
def display_time():
    increment_visits()
    moscow_time = get_moscow_time()
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=formatted_time)

@app.route('/visits')
def get_visits():
    visits = load_visits()
    return ({'visits': visits})

def get_moscow_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_utc_time = datetime.utcnow()
    moscow_time = current_utc_time.replace(tzinfo=timezone.utc).\
        astimezone(moscow_timezone)
    return moscow_time

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype="text/plain")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
