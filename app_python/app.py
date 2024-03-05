from flask import Flask

from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)
timezone = ZoneInfo('Europe/Moscow')


@app.route("/")
def index():
    return f"Current time in Moscow: {current_time()}"


def current_time():
    return datetime.now(timezone).time().isoformat('seconds')
