from flask import Flask, render_template
from datetime import datetime
import pytz
import os

app = Flask(__name__)

x = 0
@app.before_request
def count_requests():
    global x
    x += 1
    with open('visits/visits.txt', 'w') as f:
        f.write(str(x))


@app.route('/visits')
def visits():
    return render_template("visits.html", x=x)


@app.route("/")
def index():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_msc_time = datetime.now(moscow_tz).strftime("%d-%m-%Y %H:%M:%S")
    return render_template("index.html", current_msc_time=current_msc_time)


if __name__ == "__main__":
    if not os.path.exists('visits'):
        os.makedirs('visits')

    if os.path.exists('visits/visits.txt'):
        with open('visits/visits.txt', 'r') as file:
            x = int(file.read())

    app.run(debug=True, host='0.0.0.0')
