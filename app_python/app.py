from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

# In-memory storage for metric data
view_metric = {}
buy_metric = {}


# Function to get Moscow time in seconds since epoch
def get_moscow_time_seconds():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    return int(moscow_time.timestamp())


# Root route to display Moscow time
@app.route('/')
def show_time():
    moscow_time = datetime.fromtimestamp(get_moscow_time_seconds())
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
