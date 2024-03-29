import pytz
import os
import json
import logging
from flask import Flask
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
app.config['port'] = os.getenv('PORT', default=5000)
app.config['timezone'] = os.getenv('TIMEZONE', default='Europe/Moscow')
app.config['datetime_format'] = os.getenv('DATETIME_FORMAT',
                                          default='%Y-%m-%d %H:%M:%S %z')
logs_file_path = os.getenv('LOGS_FILE_PATH', default='../logs/moscow_time.log')
logging.basicConfig(filename=logs_file_path,level=logging.DEBUG)


@app.route("/health")
def status(): 
    return "UP"


@app.route("/api/v1/time")
def get_time():
    """
    method to fetch current time in a configured
     timezone in a configured format

    :return: dictionary containing "time" field or an "error" filed
    """
    try:
        timestamp = get_timestamp()
        return format_datetime_response(timestamp)
    except Exception as ex:
        app.logger.error(f'An error has occurred: {ex}')
        return json.dumps({"error": "Internal server error"}), 500


def get_timestamp() -> datetime:
    app_timezone = pytz.timezone(app.config['timezone'])
    timestamp = app_timezone.localize(datetime.now(), is_dst=None)
    return timestamp


def format_datetime_response(timestamp: datetime) -> str:
    formatted_time = timestamp.strftime(app.config['datetime_format'])
    response = json.dumps({'time': formatted_time})
    return response


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=app.config['port'])
