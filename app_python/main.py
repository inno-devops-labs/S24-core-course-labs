from flask import Flask, render_template
from datetime import datetime
from prometheus_client import generate_latest
import pytz

app = Flask(__name__)

counter = 0


@app.route('/')
def display_time():
    global counter
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')

    counter += 1
    with open('visits.txt', 'w') as file:
        file.write(str(counter))

    print(f"datetime is {moscow_time}")
    return render_template('index.html', time=moscow_time)


@app.route('/metrics')
def metrics():
    return generate_latest()


@app.route('/visits')
def visits():
    with open('visits.txt', 'r') as file:
        visits = file.read()
    return render_template('visits.html', visit_count=visits)


if __name__ == '__main__':
    print("The server is hosting on http://127.0.0.1:5001")
    app.run(host="0.0.0.0", port=5001)
