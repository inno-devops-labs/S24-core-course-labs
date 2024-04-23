from flask import Flask, render_template, request
from datetime import datetime
import pytz
from prometheus_client import generate_latest

app = Flask(__name__)

counter = 0
VISITS_FILE = '/data/visits.txt'

@app.route('/')
def home():
    global counter
    counter += 1
    with open(VISITS_FILE, 'w') as f:
        f.write(str(counter))
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    return render_template('index.html',
                           time=moscow_time.strftime('%d-%m-%Y %H:%M:%S'),
                           visits=counter)

@app.route('/visits')
def visits():
    global counter
    with open(VISITS_FILE, 'r') as f:
        visits = int(f.read())
    return str(visits)

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
