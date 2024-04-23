from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

VOLUME="volume/visits.txt"

def write_visits(visits):
    with open(VOLUME, 'a') as f:
        f.write(visits)
        f.close()


def get_visits():
    with open(VOLUME, 'a') as f:
        return int(f.read().strip())

def incr():
    vis = get_visits
    write_visits(str(vis + 1))

@app.route('/')
def index():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')

    incr()
    
    return render_template('index.html', moscow_time=moscow_time)

@app.route("/visits")
def visits():
    visits = get_visits()
    return f'Visits: {visits}\n'

if __name__ == '__main__':
    app.run(debug=False)
