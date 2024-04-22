from flask import Flask, Response
from flask import jsonify
from datetime import datetime
import pytz
import os
from prometheus_client import generate_latest


app = Flask(__name__)

visits_path = "./visits/visits.txt"

def get_visits():
    if os.path.isfile(visits_path):
        with open(visits_path, "r") as visits_file:
            return int(visits_file.read().strip())
    else:
        os.makedirs(os.path.dirname(visits_path), exist_ok=True)
        with open(visits_path, "w+") as visits_file:
            visits_file.write("0")
        return 0

def increment_visits():
    n = get_visits()
    with open(visits_path, "w") as visits_file:
        visits_file.write(str(n + 1))

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')

@app.route('/visits')
def visits():
    return Response(str(get_visits()), content_type='text/plain')

@app.route('/')
def call_time() -> str:
    time_zone = pytz.timezone('Europe/Moscow')
    increment_visits()
    return datetime.now(time_zone).time().__str__()

if __name__ == '__main__':
    
    app.run()