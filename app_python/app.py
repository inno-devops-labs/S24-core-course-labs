from flask import Flask, Response, jsonify
from datetime import datetime
from prometheus_client import generate_latest
import os
import pytz

app = Flask(__name__)

visits_path = "./visits/visits.txt"

def visits_number() -> int:
    if os.path.isfile(visits_path):
        with open(visits_path, "r") as f:
            counter = int(f.read().strip())
            return counter
    else:
        os.makedirs(os.path.dirname(visits_path), exist_ok=True)
        with open(visits_path, "w+") as f:
            f.write("0")
        return 0


def increment():
    number = visits_number()
    with open(visits_path, "w") as f:
        f.write(f"{number + 1}")

@app.route('/visits')
def visits():
    visits_json = {"visits": visits_number()}
    return jsonify(visits_json)

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')

@app.route('/')
def display_time_msk():
    timezone = pytz.timezone('Europe/Moscow')
    time_msk = datetime.now(timezone)
    print("Received request")
    return f"Current time in Moscow: " \
           f"{time_msk.strftime('%Y-%m-%d %H:%M:%S %Z')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)