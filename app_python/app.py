from flask import Flask, render_template, Response, jsonify
import datetime
import os
from prometheus_client import generate_latest

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


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')


@app.route('/visits')
def visits():
    visits_json = {"visits": visits_number()}
    return jsonify(visits_json)


@app.route('/')
def index():
    moscow_time = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=3)))
    increment()
    return render_template('index.html', moscow_time=moscow_time)


if __name__ == "__main__":
    app.run()
