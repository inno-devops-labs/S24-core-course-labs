'''
python app - moscow time
'''
import datetime
import pytz
import os
import threading
from flask import Flask, render_template, Response
from prometheus_client import generate_latest

app = Flask(__name__)
visits_mutex = threading.Lock()

# Function to read the current visit count from the file
def get_visit_count():
    try:
        with open('data/visits', 'r') as f:
            count = int(f.read())
    except FileNotFoundError:
        count = 0
    return count

# Function to update the visit count in the file
def increment_visit_count():
    visits_mutex.acquire()
    count = get_visit_count() + 1
    visits_mutex.release()
    try:
        os.mkdir("data")
    except:
        pass
    with open('data/visits', 'w') as f:
        f.write(str(count))

@app.route('/metrics')
def metrics():
    '''
    metrics
    '''
    return Response(generate_latest(), content_type='text/plain')

# Route for the home page
@app.route('/')
def home():
    '''
    home page 
    '''
    # Get the current time in Moscow
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
    increment_visit_count()

    # Render the home.html template with the current time
    return render_template('index.html', current_time=current_time)

@app.route('/visits')
def visits():
    # Get the current visit count
    visit_count = get_visit_count()

    # Render the visits.html template with the visit count
    return render_template('visits.html', visit_count=visit_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
