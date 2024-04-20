from project import create_app
from flask import render_template

from pathlib import Path
import os
import datetime
import functools
import pytz

DATA_PATH = Path(__file__).resolve().parent / 'data'
VISITS_PATH = DATA_PATH / 'visits.txt'
app = create_app(templates_path='project/templates')


def update_visits(func):
    """
    Wrapper to update current site visits
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not os.environ.get('CONFIG_TYPE', None) == 'config.TestingConfig':
            with open(VISITS_PATH, 'r') as f:
                current_visits = int(f.read())

            with open(VISITS_PATH, 'w') as f:
                f.write(str(current_visits + 1))

        return func(*args, **kwargs)

    return wrapper


@app.route('/time')
def get_time() -> str:
    """
    :return: Moscow timezone info
    """
    timezone: datetime.tzinfo = pytz.timezone('Europe/Moscow')
    moscow_time: str = datetime.datetime.now(
        timezone
    ).strftime("%d %B, %H:%M:%S")
    return moscow_time


@app.route('/')
@update_visits
def home() -> str:
    """
    :return: Rendered home page with Moscow timezone info
    """
    return render_template('index.html')


@app.route('/visits')
@update_visits
def get_visits():
    """
    :return: The number of site visits
    """
    with open(VISITS_PATH, 'r') as f:
        total_visits = int(f.read())

    return {'visits': total_visits}


def main():
    if not os.path.exists(VISITS_PATH):
        if not os.path.exists(DATA_PATH):
            os.mkdir(str(DATA_PATH))

        with open(VISITS_PATH, 'w') as f:
            f.write('0')

    app.run()


if __name__ == '__main__':
    main()
