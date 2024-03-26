from flask import Flask, render_template
from prometheus_client import Counter, Summary, generate_latest
from .time import get_formatted_moscow_time

app = Flask(__name__)

index_requests_total = Counter(
    'index_requests_total',
    'The number of requests to index page.'
)

index_request_duration_seconds = Summary(
    'index_request_duration_seconds',
    'The duration of requests to index page.'
)


@app.route("/")
@index_request_duration_seconds.time()
def home():
    index_requests_total.inc()
    return render_template("index.html", moscow_time=get_formatted_moscow_time())


@app.route("/metrics")
def metrics():
    return generate_latest()
