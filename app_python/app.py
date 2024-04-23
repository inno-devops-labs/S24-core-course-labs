import os
from flask import Flask, render_template, Response
from datetime import datetime, timezone
import pytz
from prometheus_client import Summary, generate_latest

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
VISITS_DIR = 'visits'

os.makedirs(VISITS_DIR, exist_ok=True)


def read_visit_count():
    try:
        with open('visits/visits.txt', 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        with open('visits/visits.txt', 'w') as f:
            f.write('0')
            f.close()
            return 0


def write_visit_count(count):
    with open('visits/visits.txt', 'w') as f:
        f.write(str(count))
        f.close()


def increment_visit_count():
    count = read_visit_count()
    count += 1
    write_visit_count(count)
    return count


@app.route('/visits')
def visits():
    visit_count = read_visit_count()
    return f'Total visits: {visit_count}\n'


def get_current_time():
    gmt_time = datetime.now(timezone.utc)

    gmt3_timezone = pytz.timezone('Etc/GMT-3')
    gmt3_time = gmt_time.replace(tzinfo=pytz.utc).astimezone(gmt3_timezone)

    return gmt3_time.strftime('%H:%M:%S')


@app.route('/')
@REQUEST_TIME.time()
def index():
    current_time = get_current_time()
    visit_count = increment_visit_count()
    return render_template('index.html', current_time=current_time, visit_count=visit_count)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == '__main__':
    app.run(debug=False)
