import os
from flask import Blueprint, render_template
from datetime import datetime
import pytz
from pathlib import Path

app_folder = Path(os.path.dirname(__file__))
visits_file = os.path.join(app_folder.parent, "visits_folder", "visits.txt")

count_blueprint = Blueprint('count', __name__)

def _increment_visits() -> None:
    with open(visits_file, "r") as visits_file:
        visits = int(visits_file.readline())
    with open(visits_file, "w") as visits_file:
        visits_file.write(str(visits + 1))

@count_blueprint.get("/visits")
def get_visits():
    _increment_visits()

    with open(visits_file) as visits_file:
        visits = int(visits_file.readline())

    return visits

def _create_visit():
    init_value = 0
    if not os.path.isfile(visits_file):
        with open(visits_file, "w+") as file:
            file.write(str(init_value))
