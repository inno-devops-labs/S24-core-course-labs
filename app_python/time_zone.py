from datetime import datetime
from flask import Flask
import pytz
import os

app = Flask(__name__)

counter = 0


@app.before_request
def count_requests():
    global counter
    counter += 1
    with open('visits/visits.txt', 'w') as file:
        file.write(str(counter))


@app.route('/visits')
def visits():
    return f'Number of accessed times: {counter}'


@app.route('/')
def msk_time():
    time = datetime.now(pytz.timezone('Europe/Moscow'))
    return time.strftime("Current time (MSK timezone): %H:%M:%S")


if __name__ == '__main__':
    if not os.path.exists('visits'):
        os.makedirs('visits')

    if os.path.exists('visits/visits.txt'):
        with open('visits/visits.txt', 'r') as file:
            counter = int(file.read())

    app.run(debug=True, host='0.0.0.0')
