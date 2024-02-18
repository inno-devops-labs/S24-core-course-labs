from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


def get_moscow_time():
    moscow_timezone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time


@app.route("/")
def index():
    moscow_time = get_moscow_time()
    return render_template("index.html", moscow_time=moscow_time)


if __name__ == "__main__":
    app.run(debug=True)
