from flask import Blueprint, jsonify, Response
from datetime import datetime
from pytz import timezone
from prometheus_client import Summary, generate_latest

bp = Blueprint("main", __name__, url_prefix="")

REQUEST_TIME = Summary("request_processing_time", "Time to handle request")


@bp.route("/", methods=["GET"])
@REQUEST_TIME.time()
def get_time():
    """route to return the time in moscow timezone

    Returns:
        JSON: field "time" containing the current time in Moscow.
    """
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    return jsonify({"time": moscow_time})


@bp.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
