from flask import Flask, render_template, Response
from datetime import datetime
import pytz
from prometheus_client import generate_latest, Gauge, Histogram
import time
import os
app = Flask(__name__)

REQUEST_Time = Histogram('http_request_time',
                         'HTTP Request Time', ['method', 'endpoint'])
Active_Users = Gauge('active_users', 'Number of Active Users')

VISITS_FILE_PATH = "data/visits.txt"


@app.route('/')
def show_time():
    start_time = time.time()
    moscow_timezone = pytz.timezone('Europe/Moscow')
    create_visits_file_if_not_exists()
    increment_visits()
    time_now = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
    REQUEST_Time.labels(method='GET',
                        endpoint='/').observe(time.time() - start_time)
    return render_template('time_template.html', time_now=time_now)


def increment_visits():
    with open(VISITS_FILE_PATH, "r+") as file:
        visits = int(file.read())
        visits += 1
        file.seek(0)
        file.write(str(visits))


def create_visits_file_if_not_exists():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(VISITS_FILE_PATH), exist_ok=True)
    if os.path.isfile(VISITS_FILE_PATH):
        print("Visits file already exists")
        return

    # Create the file with initial value 0
    init_value = 0
    with open(VISITS_FILE_PATH, "w+") as file:
        file.write(str(init_value))
    print(f"Visits file created with initial value {init_value}")


@app.get("/visits")
def get_visits():
    """
    Return the number of visits.
    """
    with open(VISITS_FILE_PATH, "r") as file:
        visits = int(file.read())
    return {"visitors": visits}


@app.route('/healthcheck')
def health_check():
    return Response(status=200)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=False)
