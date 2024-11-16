from flask import Flask, render_template
from datetime import datetime, timezone, timedelta
import os

app = Flask(__name__)

VISITS_FILE = 'visits.txt'


with open(VISITS_FILE, 'w') as f:
    f.write('0')

def read_visits():
    with open(VISITS_FILE, 'r') as f:
        return int(f.read().strip())

def write_visits(count):
    with open(VISITS_FILE, 'w') as f:
        f.write(str(count))

@app.route('/')
def display_time():
    # Get the current time in Moscow
    moscow_time = datetime.now(timezone(timedelta(hours=3)))

    # Format the time for display
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

    visits = read_visits()
    visits += 1
    write_visits(visits)

    # Render the template with the formatted time and visit count
    return render_template('index.html', time=formatted_time, visits=visits)

@app.route('/visits')
def display_visits():
    visits = read_visits()
    return f"The recorded number of visits is: {visits}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
