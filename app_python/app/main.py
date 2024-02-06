from flask import Blueprint, jsonify
from datetime import datetime
from pytz import timezone

bp = Blueprint("main", __name__, url_prefix="")


@bp.route("/", methods=["GET"])
def get_time():
    """route to return the time in moscow timezone

    Returns:
        JSON: field "time" containing the current time in Moscow.
    """
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    return jsonify({"time": moscow_time})
