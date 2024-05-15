from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
from datetime import datetime, timedelta
import pytz
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Initialize or read the visits count
visits_file_path = "./data/visits.txt"

def read_visits():
    if os.path.exists(visits_file_path):
        with open(visits_file_path, "r") as file:
            return int(file.read())
    return 0

def write_visits(count):
    with open(visits_file_path, "w") as file:
        file.write(str(count))

@app.route('/')
def current_time_moscow():
    # Increment visits count
    count = read_visits() + 1
    write_visits(count)

    # Get the current time in UTC
    utc_now = datetime.utcnow()

    # Get the timezone for Moscow
    moscow_tz = pytz.timezone('Europe/Moscow')

    # Convert UTC time to Moscow time
    moscow_time = utc_now + timedelta(seconds=moscow_tz.utcoffset(utc_now).seconds)

    # Render the template with the current time
    return render_template('index.html', current_time=moscow_time.strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/visits')
def visits():
    # Read the current visit count
    visits = read_visits()
    return f"The page has been visited {visits} times"

if __name__ == '__main__':
    app.run(debug=True)
