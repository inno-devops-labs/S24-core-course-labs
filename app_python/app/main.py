from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIMEZONE = "Europe/Moscow"


def get_time(timezone):
    return datetime.now(timezone)


def format_time(time, time_format):
    return time.strftime(time_format)


@app.route("/")
def home():
    timezone = pytz.timezone(TIMEZONE)
    time = get_time(timezone)
    time_string = format_time(time, TIME_FORMAT)
    return render_template("index.html", moscow_time=time_string)


if __name__ == "__main__":
    app.run(debug=True)
