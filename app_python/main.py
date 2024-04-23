"""
Current Moscow time app
"""
import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)
visit_count = 0

@app.route('/visits')
def visits():
    global visit_count
    return f'Total visits: {visit_count}'

try:
    with open('data/visits.txt', 'r') as f:
        visit_count = int(f.read())
except FileNotFoundError:
    visit_count = 0

def save_visit_count(count):
    with open('data/visits.txt', 'w') as f:
        f.write(str(count))


@app.route('/')
def display_time():
    """
    Display Moscow time
    """
    global visit_count
    visit_count += 1
    save_visit_count(visit_count)
    moscow = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=current_time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
