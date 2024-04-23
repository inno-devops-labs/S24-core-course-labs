from flask import Flask, jsonify
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')
VISITS_FILE = os.getenv('FILE')


def load_visits():
    try:
        with open(VISITS_FILE, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0


def save_visits(visits):
    with open(VISITS_FILE, 'w') as file:
        file.write(str(visits))


@app.route('/')
def get_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f'The current time in Moscow is: {current_time}'


@app.route('/visits')
def get_visits():
    visits = load_visits()
    return jsonify({'visits': visits})


@app.before_request
def increment_visit():
    visits = load_visits()
    visits += 1
    save_visits(visits)


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
