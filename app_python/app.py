from flask import Flask, render_template, jsonify
from datetime import datetime, timezone, timedelta
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

VISITS_FILE = os.path.join(os.path.dirname(__file__), "data", "visits.txt")


def get_moscow_time():
    moscow_timezone = timezone(timedelta(hours=3))  # Moscow is UTC+3
    current_time = datetime.now(moscow_timezone)
    return current_time.strftime("%Y.%m.%d %H:%M:%S")


# Function to safely increment visit count
def increment_visit_count():
    try:
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'r+') as file:
                count_str = file.read().strip()
                if count_str:
                    count = int(count_str)
                else:
                    count = 0
                file.seek(0)
                file.write(str(count + 1))
                file.truncate()
        else:
            with open(VISITS_FILE, 'w') as file:
                file.write('1')
    except Exception as e:
        print(f"Error occurred while incrementing visit count: {e}")


# Function to read visit count
def get_visit_count():
    try:
        if os.path.exists(VISITS_FILE):
            with open(VISITS_FILE, 'r') as file:
                count_str = file.read().strip()
                if count_str:
                    return int(count_str)
                else:
                    return 0
        else:
            return 0
    except Exception as e:
        print(f"Error occurred while reading visit count: {e}")
        return 0


# The root URL of the app
@app.route('/')
def index():
    increment_visit_count()
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)


@app.route('/visits')
def visits():
    visit_count = get_visit_count()
    return jsonify({'visits': visit_count})


if __name__ == '__main__':
    app.run(debug=True)
