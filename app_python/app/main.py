import os

from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIMEZONE = "Europe/Moscow"
HOSTNAME = "0.0.0.0"
VISITS_FILE_PATH = "data/visits.txt"


def get_time(timezone):
    return datetime.now(timezone)


def format_time(time, time_format):
    return time.strftime(time_format)


@app.get("/visits")
def get_visits():
    """
    Return the number of visits.
    """
    with open(VISITS_FILE_PATH, "r") as file:
        visits = int(file.read())
    return {"visits": visits}


def increment_visits():
    with open(VISITS_FILE_PATH, "r+") as file:
        visits = int(file.read())
        visits += 1
        file.seek(0)
        file.write(str(visits))


def create_visits_file_if_not_exists():
    if os.path.isfile(VISITS_FILE_PATH):
        print("Visits file already exists")
        return

    init_value = 0
    with open(VISITS_FILE_PATH, "w+") as file:
        file.write(str(init_value))

    print(f"Visits file created with initial value {init_value}")

@app.route("/")
def home():
    increment_visits()
    timezone = pytz.timezone(TIMEZONE)
    time = get_time(timezone)
    time_string = format_time(time, TIME_FORMAT)
    return render_template("index.html", moscow_time=time_string)


if __name__ == "__main__":
    create_visits_file_if_not_exists()
    app.run(host=HOSTNAME, port=3000, debug=True)
