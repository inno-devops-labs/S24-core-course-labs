import datetime
from time import monotonic

from flask import Flask, request, Response
import requests
import prometheus_client

from .cache import cache_for


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


@app.route('/')
def index():
    time = get_time()
    return f"In MSK it's {time.hour}:{time.minute}:{time.second}. " \
        "Have you brushed your teeth today yet?"

@app.route('/metrics')
def prometheus_metrics():
    return Response(prometheus_client.generate_latest(), mimetype='text/plain')
