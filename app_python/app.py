from flask import Flask, Response, jsonify
from datetime import datetime
from pytz import timezone
from prometheus_client import generate_latest

app = Flask(__name__)
VISIT_COUNT = 0

@app.route("/visits", methods=["GET"])
def get_visits():
    global VISIT_COUNT
    return jsonify({"visit_count": VISIT_COUNT})

try:
    with open('visits.txt', 'r') as f:
        VISIT_COUNT = int(f.read())
except FileNotFoundError:
    VISIT_COUNT = 0

def save_visit_count(count):
    with open('visits.txt', 'w') as f:
        f.write(str(count))

@app.route('/')
def show_time():
    global VISIT_COUNT
    VISIT_COUNT += 1
    save_visit_count(VISIT_COUNT)
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    return jsonify({"time": moscow_time})

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
