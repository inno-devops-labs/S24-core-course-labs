from flask import Flask, render_template, Response
from datetime import datetime
import pytz
import os
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

# Define your metrics
REQUEST_COUNT = Counter('app_request_count', 'Total web app request count')
REQUEST_TIME = Gauge('moscow_time_seconds', 'Moscow time in seconds')


def getMoscowTime(timezone='Europe/Moscow'):
    moscow_tz = pytz.timezone(timezone)
    moscow_time = datetime.now(moscow_tz)
    return moscow_time


# Ensure data/visits file exists
if not os.path.exists('data/visits'):
    os.mkdir("data")
    with open('data/visits', 'a+') as f:
        f.write('0')


@app.route('/')
def show_time():
    REQUEST_COUNT.inc()  # Increment the count for each request
    moscow_time = getMoscowTime('Europe/Moscow')

    # Set the gauge to current Moscow time in seconds past the minute
    REQUEST_TIME.set(moscow_time.second + moscow_time.minute * 60 + moscow_time.hour * 3600)

    # Render the time in a human-friendly format
    formatted_moscow_time = moscow_time.strftime('%H:%M:%S')

    # write the count to visits file
    with open('data/visits', 'w') as f:
        f.write(str(REQUEST_COUNT._value.get()))

    return render_template('time.html', time_in_moscow=formatted_moscow_time)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')


@app.route('/visits')
def visits():
    # get visits count from the visits file
    with open('data/visits', 'r') as f:
        visits_count = f.read()
    return Response("Total visits: " + str(visits_count), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
