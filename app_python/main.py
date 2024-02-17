import datetime
from zoneinfo import ZoneInfo
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    time_zone = ZoneInfo("Europe/Moscow")
    return datetime.datetime.now(time_zone).strftime("%H:%M:%S")

if __name__ == "__main__":
    from waitress import serve
    serve(app)