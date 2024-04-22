from datetime import datetime
import pytz
from flask import Flask
import os

app = Flask(__name__)

counter = 0

if not os.path.exists('visits'):
    os.makedirs('visits')

if os.path.exists('visits/visits.txt'):
    with open('visits/visits.txt', 'r') as file:
        counter = int(file.read())

@app.before_request
def count_requests():
    global counter
    counter += 1
    with open('visits/visits.txt', 'w') as file:
        file.write(str(counter))

@app.route('/visits')
def visits():
    return f'Number of page visits: {counter}'

@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/")
def display_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time_moscow = datetime.now(moscow_tz)
    formatted_time = current_time_moscow.strftime('%Y-%m-%d %H:%M:%S %Z')
    return f"Current time in Moscow: {formatted_time}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
