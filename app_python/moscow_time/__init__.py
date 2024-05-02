import datetime
from os import makedirs
from time import monotonic

from flask import Flask, request, Response, send_from_directory
import requests
import prometheus_client

from .cache import cache_for
from .visits import increment_on_call


app = Flask(__name__)


REQUEST_COUNT = prometheus_client.Counter('py_requests_count', 'Number of HTTP requests')
REQUEST_HANDLE_TIME = prometheus_client.Histogram('py_request_handle_time', 'Time to handle a request')

@app.before_request
def note_request_start_time():
    request.start_time = monotonic()

@app.after_request
def update_prometheus(response):
    handle_time = monotonic() - request.start_time
    REQUEST_COUNT.inc()
    REQUEST_HANDLE_TIME.observe(handle_time)
    return response


# In case of high load, to avoid frequent requests, cache results for
# one second
@cache_for(1000)
def get_time():
    """
    Get current Moscow time from worldtimeapi.org.

    The returned value is of type `datetime.time` and it may be up to
    1000ms out of date, as results of calls to the function are cached
    for up to 1 second.
    """
    r = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    dt = datetime.datetime.fromisoformat(r.json()['datetime'])
    return dt.time()


VISITS_FILENAME = 'persistent/visits.bin'

# Create it on start
try:
    basename_at = VISITS_FILENAME.rindex('/')
except ValueError:
    pass
else:
    makedirs(VISITS_FILENAME[:basename_at], exist_ok=True)
open(VISITS_FILENAME, 'a+').close()  # The `a+` mode ensures we have write perm


@app.route('/')
@increment_on_call(VISITS_FILENAME)
def index():
    time = get_time()
    return f"In MSK it's {time.hour}:{time.minute}:{time.second}. " \
        "Have you brushed your teeth today yet?"

@app.route('/metrics')
@increment_on_call(VISITS_FILENAME)
def prometheus_metrics():
    return Response(prometheus_client.generate_latest(), mimetype='text/plain')

@app.route('/visits')
@increment_on_call(VISITS_FILENAME)
def visits():
    with open(VISITS_FILENAME, 'rb') as f:
        return str(int.from_bytes(f.read(), byteorder='little'))
