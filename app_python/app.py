from flask import Flask, render_template
from datetime import datetime, timezone, timedelta
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

def get_moscow_time():
    moscow_timezone = timezone(timedelta(hours=3))  # Moscow is UTC+3
    current_time = datetime.now(moscow_timezone)
    return current_time.strftime("%Y.%m.%d %H:%M:%S")


# The root URL of the app
@app.route('/')
def index():
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)

if __name__ == '__main__':
    app.run(debug=True)
