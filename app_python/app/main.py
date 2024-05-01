from flask import Blueprint, jsonify, Response
from datetime import datetime
from pytz import timezone
from prometheus_client import Summary, generate_latest
import os

bp = Blueprint("main", __name__, url_prefix="")

REQUEST_TIME = Summary("request_processing_time", "Time to handle request")

@bp.route("/visits", methods=["GET"])
def get_visits():
    """route to return the website visist count
    """
    if not os.path.exists('./app/visits.txt'):
        with open('./app/visits.txt', 'w') as f:
            f.write('0')
    with open('./app/visits.txt', 'r') as f:
        VISIT_COUNT = int(f.readline())
    return jsonify({"visit_count": VISIT_COUNT})

def save_visit_count():
    if not os.path.exists('/app/visits.txt'):
        with open('./app/visits.txt', 'w') as f:
            f.write('0')
    with open('./app/visits.txt', 'r') as f:
        VISIT_COUNT = int(f.readline())
    with open('./app/visits.txt', 'w') as f:
        f.write(str(VISIT_COUNT+1))

@bp.route("/", methods=["GET"])
@REQUEST_TIME.time()
def get_time():
    """route to return the time in moscow timezone

    Returns:
        JSON: field "time" containing the current time in Moscow.
    """
    save_visit_count()
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    return jsonify({"time": moscow_time})


@bp.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
