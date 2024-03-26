from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
from datetime import datetime
import pytz

app = Flask(__name__)
metrics = PrometheusMetrics(app)


def get_moscow_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def index():
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
