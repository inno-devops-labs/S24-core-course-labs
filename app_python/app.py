from flask import Flask, jsonify, Response
from datetime import datetime
from prometheus_client import generate_latest
import pytz
import os
import threading

app = Flask(__name__)

counter = 0

data_folder = 'data'
visits_file = os.path.join(data_folder, 'visits.txt')


def save_visits_to_file():
    global counter
    if not os.path.exists("data"):
        os.mkdir("data")
    with open(visits_file, 'w') as f:
        f.write(str(counter))


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')


@app.route('/')
def index():
    global counter
    counter += 1
    save_visits_to_file()
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'time_in_moscow': formatted_time})


@app.route('/visits')
def visits():
    with open(visits_file, 'r') as f:
        visits_count = int(f.read())
    return jsonify({'total_visits': visits_count})


if __name__ == '__main__':
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    if not os.path.exists(visits_file):
        with open(visits_file, 'w') as f:
            f.write('0')

    threading.Thread(target=save_visits_to_file, daemon=True).start()

    app.run(host="0.0.0.0", port=5000)
