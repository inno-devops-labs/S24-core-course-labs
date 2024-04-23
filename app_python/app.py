from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
from datetime import datetime
import pytz

app = Flask(__name__)
metrics = PrometheusMetrics(app)
visits_file = "visits.txt"

def read_visit_count():
    try:
        with open(visits_file, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open(visits_file, "w") as file:
            file.write("0")
        return 0
    
visit_count = read_visit_count()

def get_moscow_time():
    global visit_count
    visit_count += 1

    with open(visits_file, "w") as file:
        file.write(str(visit_count))

    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def index():
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)

@app.route("/visits")
def display_visits():
    global visit_count
    return f"Total visits: {visit_count}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
