"""
This module defines a Flask application to display the current time in Moscow.
"""
import os
from datetime import datetime
import pytz
from flask import Flask, Response
from prometheus_client import generate_latest

app = Flask(__name__)
VISITS_FILE = "./data/visits.txt"

def increment_visits():
    """
    Increment number of visits and write to file
    """
    if not os.path.exists(VISITS_FILE):
        os.mkdir(os.path.dirname(VISITS_FILE))
        with open(VISITS_FILE, "w", encoding="utf-8") as f:
            f.write("0")

    with open(VISITS_FILE, "r+", encoding="utf-8") as f:
        visits_cnt = str(int(f.read()) + 1)
        f.seek(0)
        f.write(visits_cnt)

# Define a route to display the current time in Moscow
@app.route('/')
def display_time():
    """
    Display the current time in Moscow.
    """
    increment_visits()

    city_timezone = pytz.timezone('Europe/Moscow')
    city_time = datetime.now(city_timezone)
    formatted_city_time = city_time.strftime('%Y-%m-%d %H:%M:%S')
    return f'Current time in the city: {formatted_city_time}'


@app.route("/metrics")
def metrics():
    """
    Returns Prometheus metrics
    """
    return Response(generate_latest(), mimetype='text/plain')


@app.route("/visits")
def visits():
    """
    Returns number of visits
    """
    with open(VISITS_FILE, "r", encoding="utf-8") as f:
        return {'visits': int(f.read())}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
