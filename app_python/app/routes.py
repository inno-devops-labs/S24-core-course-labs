from flask import Flask, render_template, jsonify, Response
from datetime import datetime, timedelta
import pytz
from prometheus_client import generate_latest
import os

app = Flask(__name__, template_folder='templates', static_folder='../static')

VISITS_FILE = "./visits/visits.txt"

def reset():    
    directory = os.path.dirname(VISITS_FILE)
    os.makedirs(directory, exist_ok=True)
    with open(VISITS_FILE, "w+") as file:
        file.write("0")

def read_visits():
    if os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "r") as file:
            return int(file.read().strip())
    return 0

def inc_visits(count):
    with open(VISITS_FILE, "w+") as file:
        file.write(str(count))

reset()
visit_count = read_visits()

@app.route('/')
def index():
    """
    Render the index.html template and increment visits.

    Returns:
        rendered HTML template
    """
    global visit_count
    visit_count += 1
    inc_visits(visit_count)
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')

@app.route('/get_time')
def get_time():
    """
    Get the current time in Moscow timezone and return it as JSON.

    Returns:
        JSON response containing Moscow time
    """
    moscow_time = get_moscow_time()
    return jsonify({'moscow_time': moscow_time})

def get_moscow_time():
    """
    Get the current time in Moscow timezone and format it.

    Returns:
        Formatted string representing the current Moscow time
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time

@app.route('/visits')
def visits():
    """
    Display the number of visits.

    Returns:
        Text stating how many times the application has been accessed.
    """
    global visit_count
    visit_count += 1
    inc_visits(visit_count)
    return f"Number of visits {visit_count}."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)