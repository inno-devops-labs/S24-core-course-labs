from flask import Blueprint, render_template
from datetime import datetime
import pytz

time_blueprint = Blueprint('time', __name__)

@time_blueprint.route('/')
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    time_string = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=time_string)
