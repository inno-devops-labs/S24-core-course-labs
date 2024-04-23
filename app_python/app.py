import os
from datetime import datetime

import pytz
from flask import Flask, render_template

app = Flask(__name__)

timezone_country = 'Europe/Moscow'
visits_file_path = os.getenv("VISITS_FILE", 'visits.txt')

@app.route('/')
def display_time():
    inc_counter()
    return render_template('index.html', current_time=get_time('Europe/Moscow'), country=timezone_country)

@app.route('/visits')
def display_visits():
    return str(get_counter())

def get_time(timezone_name):
    timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    return current_time

def inc_counter():
    counter = get_counter() + 1
    with open(visits_file_path, 'w') as file:
        file.write(str(counter))

def get_counter():
    try:
        with open(visits_file_path, 'r') as file:
            visits = file.read()
        return int(visits)
    except Exception:
        return 0


if __name__ == '__main__':
    app.run()
