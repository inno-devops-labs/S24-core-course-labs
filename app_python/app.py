from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def index():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_msc_time = datetime.now(moscow_tz).strftime("%d-%m-%Y %H:%M:%S")
    return render_template("index.html", current_msc_time=current_msc_time)


if __name__ == "__main__":
    app.run()
