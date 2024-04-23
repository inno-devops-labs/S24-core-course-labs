import pytz
from flask import Flask, render_template
from datetime import datetime

from services.time_service import TimeService
from services.visit_counter_service import VisitCounterService

app = Flask(__name__)

visit_counter_service = VisitCounterService()

@app.route('/')
def display_current_time():
    visit_counter_service.increment()
    moscow_time = TimeService('Europe/Moscow')
    current_time = moscow_time.get_current_time_str()
    return render_template('index.html', current_time=current_time)


@app.route('/visits')
def display_visits():
    return str(visit_counter_service.get())


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
