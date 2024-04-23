from flask import Blueprint, render_template

from api.services.visits import get_visits


visits = Blueprint('/visits', __name__)

@visits.route('/visits')
def get_visits_endpoint():
    return render_template("visits.html", visits=get_visits())