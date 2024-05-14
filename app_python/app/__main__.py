"""
Routing of the app
"""

from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
from utils import get_moscow_time

app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='endpoint')


@app.route('/')
@metrics.counter(
    'cnt_collection', 'Number of invocations per collection', labels={
        'status': lambda resp: resp.status_code
    })
def index():
    """Render funtion for start page of the app"""
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
