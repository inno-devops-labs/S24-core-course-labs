from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
from prometheus_client import generate_latest
import os

app = Flask(__name__)

visits_file = 'data/visits.txt'

def get_visits_count():
    if not os.path.exists(visits_file):
        return 0
    with open(visits_file, 'r') as f:
        count = int(f.read().strip())
    return count

def increment_visits_count():
    count = get_visits_count()
    count += 1
    with open(visits_file, 'w') as f:
        f.write(str(count))

@app.route('/')
def index():
    moscow_time = datetime.now(timezone(timedelta(hours=3)))
    increment_visits_count()
    return render_template('index.html',
                           time=moscow_time.strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/visits')
def visits():
    count = get_visits_count()
    return f'Total visits: {count}'

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)
