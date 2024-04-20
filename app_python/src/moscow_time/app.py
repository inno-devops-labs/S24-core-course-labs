from flask import Flask, Response
from datetime import datetime
import pytz
from prometheus_client import generate_latest, Counter
import os
from config import visits_file


app = Flask(__name__)

healthcheck_counter = Counter(
    'healthcheck_requests',
    'Number of healthcheck requests'
)

@app.route('/')
def display_time():
    increment_visits()
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f'The current time in Moscow is: {current_time}'

@app.route("/visits")
def visits():
    """
    Returns number of visits
    """
    with open(visits_file, "r") as f:
        return {'visits': int(f.read())}

def increment_visits():
    """
    Increment number of visits and write to file
    """
    if not os.path.exists(visits_file):
        os.mkdir(os.path.dirname(visits_file))
        with open(visits_file, "w") as f:
            f.write("0")

    with open(visits_file, "r+") as f:
        visits_cnt = str(int(f.read()) + 1)
        f.seek(0)
        f.write(visits_cnt)


@app.route('/healthcheck')
def healthcheck():
    healthcheck_counter.inc()
    return 'Ok'


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
