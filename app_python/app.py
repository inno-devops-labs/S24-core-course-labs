from flask import Flask, render_template
from datetime import datetime
import pytz
import os
import threading


app = Flask(__name__)
visits_mutex = threading.Lock()


def get_visits():
    with open('data/visits', 'r') as f:
        return int(f.read())
    

def increment_visits():
    visits_mutex.acquire()
    visits = get_visits() + 1
    visits_mutex.release()
    with open('visits', 'w') as f:
        f.write(str(visits))


def get_moscow_time():
    moscow_timezone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time


@app.route("/")
def index():
    increment_visits()
    moscow_time = get_moscow_time()
    return render_template("index.html", moscow_time=moscow_time)


@app.route('/visits')
def visits():
    visits_count = get_visits()
    return render_template('visits.html', visits_count=visits_count)


if __name__ == "__main__":
    app.run(debug=True)
