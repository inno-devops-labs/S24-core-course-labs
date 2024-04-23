import os

from flask import Flask, render_template
from datetime import datetime, timezone, timedelta


PATH_VISITS = "data/visits.txt"


app = Flask(__name__, template_folder="./templates")


def get_visits():
    with open(PATH_VISITS, "r") as f:
        n_visits = int(f.read())

    return n_visits

def increment_visits():
    n_visits = get_visits() + 1

    with open(PATH_VISITS, "w") as f:
        f.write(str(n_visits))

    return n_visits


@app.route('/')
def display_time():
    increment_visits()

    moscow_time = datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=3)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

    return render_template('index.html', time=formatted_time)

@app.route('/visits')
def display_visits():
    return f"Number of visits: {get_visits()}"


if __name__ == '__main__':
    if not os.path.isfile(PATH_VISITS):
        with open(PATH_VISITS, "w+") as f:
            f.write("0")

    app.run(host= '0.0.0.0', port=5000)