from flask import Flask, render_template
from datetime import datetime
import pytz
from prometheus_client import generate_latest
import os

app = Flask(__name__)
counter_file_path = '/data/visits.txt'

def read_counter():
    try:
        with open(counter_file_path, 'r') as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 0

def write_counter(value):
    with open(counter_file_path, 'w') as file:
        file.write(str(value))

@app.route('/')
def index():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    
    current_visits = read_counter()
    write_counter(current_visits + 1)
    
    return render_template('index.html', time=moscow_time, visits=current_visits)

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/visits')
def show_visits():
    visits = read_counter()
    return f"Number of visits: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
