from flask import Blueprint, render_template

from app_python.api.services.visits import get_visits


visits = Blueprint('/visits', __name__)

@visits.route('/')
def visits():
    return render_template("visits.html", visits=get_visits())