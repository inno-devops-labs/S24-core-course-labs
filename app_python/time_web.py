from flask import Flask, Response
from datetime import datetime
import pytz
from prometheus_client import generate_latest, Counter
import os

app = Flask(__name__)
VISIT_COUNTER = "visit_counter.txt"

healthcheck_counter = Counter(
    'healthcheck_requests',
    'Number of healthcheck requests'
)


@app.route('/')
def get_time():
    visit()
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    return f"The current time in Moscow is: {moscow_time}"


@app.route('/healthcheck')
def healthcheck():
    healthcheck_counter.inc()
    return 'Ok'


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')


@app.get("/visits")
def visit_count():
    with open(VISIT_COUNTER, "r") as file:
        visits = int(file.read())
    return f"Total visits: {visits}"


def visit():
    with open(VISIT_COUNTER, "r") as file:
        visits = int(file.read()) + 1

    with open(VISIT_COUNTER, "w") as file:
        file.write(str(visits))

    return visits


def creating_file():
    if os.path.isfile(VISIT_COUNTER):
        return

    with open(VISIT_COUNTER, "w+") as file:
        file.write(str(0))




if __name__ == '__main__':
    creating_file()
    app.run(host='0.0.0.0', port=5000)
