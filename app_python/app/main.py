from flask import Blueprint, jsonify, Response
from datetime import datetime
from pytz import timezone
from prometheus_client import Summary, generate_latest

bp = Blueprint("main", __name__, url_prefix="")

REQUEST_TIME = Summary("request_processing_time", "Time to handle request")
VISIT_COUNT = 0

@bp.route("/visits", methods=["GET"])
def get_visits():
    """route to return the website visist count
    """
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

@bp.route("/", methods=["GET"])
@REQUEST_TIME.time()
def get_time():
    """route to return the time in moscow timezone

    Returns:
        JSON: field "time" containing the current time in Moscow.
    """
    global VISIT_COUNT
    VISIT_COUNT += 1
    save_visit_count(VISIT_COUNT)
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    return jsonify({"time": moscow_time})


@bp.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
