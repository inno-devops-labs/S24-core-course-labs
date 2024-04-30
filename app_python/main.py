import os.path
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.0')

VISITS_FILE_PATH = "/app/vol/visits"


def log_visit() -> int:
    if not os.path.isfile(VISITS_FILE_PATH):
        with open(VISITS_FILE_PATH, "w"):
            pass

    with open(VISITS_FILE_PATH, "r+") as visits_file:
        l = visits_file.readline()
        if l == "":
            l = "0"
        visits_file.seek(0)
        visits = int(l) + 1
        visits_file.write(str(visits))
        return visits


@app.route('/', methods=['GET'])
def index():
    """
    :return: Current Moscow time
    """
    log_visit()
    mos_date_time = datetime.now(ZoneInfo("Europe/Moscow"))
    return mos_date_time.isoformat()


@app.route('/visits', methods=['GET'])
def visits():
    """
    :return: Visits count
    """
    return str(log_visit())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
