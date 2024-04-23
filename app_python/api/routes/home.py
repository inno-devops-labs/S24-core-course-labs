from flask import Blueprint, render_template

from api.services.moscow_time import get_current_moscow_time_str
from api.services.visits import increment_visits


home = Blueprint('/', __name__)

@home.route('/')
def current_moscow_time():
    increment_visits()
    cur_time_str = get_current_moscow_time_str()
    return render_template("current_moscow_time.html", time=cur_time_str)