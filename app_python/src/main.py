"""
This application returns Moscow time
"""

from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)

VISITS = 0

@app.route("/")
def get_time():
    """Get and save visits and Moscow time"""
    global VISITS
    try:
        with open("../visits.txt", "r", encoding="utf-8") as f:
            VISITS = int(f.read().strip())
    except FileNotFoundError:
        VISITS = 0
    VISITS += 1
    with open("../visits.txt", "w", encoding="utf-8") as f:
        f.write(str(VISITS))
    date_time = datetime.now(pytz.timezone("Europe/Moscow"))
    formatted_time = date_time.strftime("%H:%M:%S")
    return f'Moscoe time: {formatted_time}'

@app.route("/visits")
def get_visits():
    """Get and return visits"""
    try:
        with open("../visits.txt", "r", encoding="utf-8") as f:
            total_visits = int(f.read().strip())
    except FileNotFoundError:
        total_visits = 0
    return f'Total visits: {total_visits}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
