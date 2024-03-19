import pytz
from flask import Flask, render_template
from datetime import datetime

from services.time_service import TimeService

app = Flask(__name__)


@app.route('/')
def display_current_time():
    moscow_time = TimeService('Europe/Moscow')
    current_time = moscow_time.get_current_time_str()
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
