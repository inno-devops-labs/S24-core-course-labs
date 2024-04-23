from datetime import datetime
import pytz
from flask import Flask
import os

app = Flask(__name__)

counter = 0

@app.before_request
def count_requests():
    global counter
    counter += 1
    with open('visits/visits.txt', 'w') as file:
        file.write(str(counter))

@app.get("/msk_timezone")
def msk_timezone():
    time = datetime.now(pytz.timezone("Europe/Moscow"))
    return time.strftime("Current time (MSK timezone): %H:%M:%S")

@app.route('/visits')
def visits():
    return f'Number of times this application was accessed: {counter}'

@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    if not os.path.exists('visits'):
        os.makedirs('visits')

    if os.path.exists('visits/visits.txt'):
        with open('visits/visits.txt', 'r') as file:
            counter = int(file.read())

    app.run(debug=True, host='0.0.0.0')