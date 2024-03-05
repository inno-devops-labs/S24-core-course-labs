import datetime
import os
from zoneinfo import ZoneInfo
from flask import Flask

app = Flask(__name__)

def get_moscow_time():
    time_zone = ZoneInfo("Europe/Moscow")
    return datetime.datetime.now(time_zone).strftime("%H:%M:%S")

@app.route("/")
def index():
    return get_moscow_time()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    from waitress import serve
    serve(app, port=port)