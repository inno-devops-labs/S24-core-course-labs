import os
from flask import Blueprint, render_template
from datetime import datetime
import pytz

count_blueprint = Blueprint('count', __name__)

def _increment_visits() -> None:
    with open("visits_folder/visits", "r") as visits_file:
        visits = int(visits_file.readline())
    with open("visits_folder/visits", "w") as visits_file:
        visits_file.write(str(visits + 1))

@count_blueprint.get("/visits")
def get_visits():
    _increment_visits()

    with open("visits_folder/visits") as visits_file:
        visits = int(visits_file.readline())

    return visits

def _create_visit():
    init_value = 0
    if not os.path.isfile("visits_folder/visits"):
        with open("visits_folder/visits", "w+") as file:
            file.write(str(init_value))
