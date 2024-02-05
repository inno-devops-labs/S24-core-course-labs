from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/time")
def hello_world():
    tz = pytz.timezone("Europe/Moscow")
    return str(tz.localize(datetime.now(), is_dst=None))
