import pytz
from flask import Flask, render_template, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import datetime

app = Flask(__name__, template_folder='templates')

visit_counter = Counter(
    'app_visits_total',
    'Total number of visits to the application'
)


@app.route('/visit')
def visit():
    visit_counter.inc()
    return 'Visit recorded successfully!', 200


@app.route('/visits')
def visits():
    visits_count = visit_counter._value.get()
    return jsonify({'visits': visits_count}), 200


@app.route('/metrics')
def prometheus_metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


@app.route('/')
def home():
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
