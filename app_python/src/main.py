"""
This application returns Moscow time
"""

from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)

visits = 0

@app.route("/")
def get_time():
    global visits
    try:
        with open("../visits.txt", "r") as f:
            visits = int(f.read().strip())
    except FileNotFoundError:
        visits = 0
    visits += 1
    with open("../visits.txt", "w") as f:
        f.write(str(visits))
    """Get and return Moscow time"""
    date_time = datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_time = date_time.strftime("%H:%M:%S")
    return f'Moscoe time: {formatted_time}'

@app.route("/visits")
def get_visits():
    try:
        with open("../visits.txt", "r") as f:
            visits = int(f.read().strip())
    except FileNotFoundError:
        visits = 0
    return f'Total visits: {visits}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
