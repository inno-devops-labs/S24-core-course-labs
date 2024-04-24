import os
from flask import Blueprint, render_template, Response
from datetime import datetime
import pytz
from pathlib import Path

app_folder = Path(os.path.dirname(__file__))
visits_file_path = os.path.join(app_folder.parent, "visits_folder", "visits.txt")

count_blueprint = Blueprint('count', __name__)

def _increment_visits() -> None:
    with open(visits_file_path, "r") as visits_file:
        visits = int(visits_file.readline())
    with open(visits_file_path, "w") as visits_file:
        visits_file.write(str(visits + 1))


@count_blueprint.route('/visits', methods=['GET'])
def get_visits():
    _increment_visits()

    with open(visits_file_path) as visits_file:
        visits = int(visits_file.readline())

    return Response(str(visits), content_type='text/plain')

def _create_visit():
    init_value = 0
    if not os.path.isfile(visits_file_path):
        with open(visits_file_path, "w+") as file:
            file.write(str(init_value))
