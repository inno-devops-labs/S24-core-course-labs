from flask import Flask
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# In-memory storage for metric data
view_metric = {}
buy_metric = {}

# File to store the visit counter
VISIT_FILE = 'visits/visits.txt'

# Initialize the counter from the file (if it exists)
counter = 0
if os.path.exists(VISIT_FILE):
    with open(VISIT_FILE, 'r') as file:
        counter = int(file.read().strip())


# Function to get Moscow time in seconds since epoch
def get_moscow_time_seconds():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    return int(moscow_time.timestamp())


# Update the visit counter and save it to the file
def update_visit_count():
    global counter
    counter += 1
    with open(VISIT_FILE, 'w') as file:
        file.write(str(counter))


# Root route to display Moscow time
@app.route('/')
def show_time():
    moscow_time = datetime.fromtimestamp(get_moscow_time_seconds())
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    update_visit_count()  # Increment visit counter on each access
    return f"<h1>Moscow Time: {formatted_time}</h1>"


# Metrics route for Prometheus scraping
@app.route('/metrics')
def metrics():
    # Create a formatted metric string for current Moscow time
    metrics_output = f"# HELP moscow_time_seconds Current Moscow time in seconds since epoch\n"
    metrics_output += f"# TYPE moscow_time_seconds gauge\n"
    metrics_output += f"moscow_time_seconds {get_moscow_time_seconds()}\n"

    # Optional: Add custom metrics for views and buys, if applicable
    for id, count in view_metric.items():
        metrics_output += f'view_total{{product="{id}"}} {count}\n'
    for id, count in buy_metric.items():
        metrics_output += f'buy_total{{product="{id}"}} {count}\n'

    return metrics_output, 200, {'Content-Type': 'text/plain'}


# Visits route to display the visit count
@app.route('/visits')
def visits():
    return f'Number of accessed times: {counter}'


if __name__ == '__main__':
    # Ensure the visits directory exists
    if not os.path.exists('visits'):
        os.makedirs('visits')

    app.run(debug=True, host='0.0.0.0', port=8080)