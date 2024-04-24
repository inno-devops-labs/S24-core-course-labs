import os
import pathlib
from flask import Flask, Response, render_template
from prometheus_client import Counter, Summary, generate_latest
from .time import get_formatted_moscow_time

app = Flask(__name__)
data_dir_path = pathlib.Path(__file__).parent.parent.resolve() / "data"

index_requests_total = Counter(
    'index_requests_total',
    'The number of requests to index page.'
)

index_request_duration_seconds = Summary(
    'index_request_duration_seconds',
    'The duration of requests to index page.'
)


def read_visits() -> int:
    os.makedirs(data_dir_path, exist_ok=True)
    try:
        with open(data_dir_path / "visits", "r") as f:
            return int(f.read().strip())
    except (ValueError, FileNotFoundError):
        return 0


def increment_visits():
    visits = read_visits()
    with open(data_dir_path / "visits", "w") as f:
        f.write(str(visits + 1))


@app.route("/")
@index_request_duration_seconds.time()
def home():
    index_requests_total.inc()

    increment_visits()

    return render_template("index.html", moscow_time=get_formatted_moscow_time())


@app.route("/visits")
def visits():
    return Response(str(read_visits()))


@app.route("/metrics")
def metrics():
    return generate_latest()
