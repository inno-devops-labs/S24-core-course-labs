# app.py

from flask import Flask, render_template, Response
from datetime import datetime
import pytz
from prometheus_client import start_http_server, Summary, Counter
import prometheus_client

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
VISIT_COUNTER = Counter('visits_total', 'Total number of visits')

app = Flask("Moscow_current_time")

# Tell Flask to look for static files in the 'static' folder
app.static_folder = 'static'

VISITS_FILE_PATH = 'data/visits.txt'


def save_visit_count(count):
    with open(VISITS_FILE_PATH, 'w') as f:
        f.write(str(count))

def get_visit_count():
    try:
        with open(VISITS_FILE_PATH, 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

visit_count = 0

@app.route('/')
@REQUEST_TIME.time()
def index():
    ##global visit_count
    try:
        visit_count = get_visit_count()
        visit_count += 1
        save_visit_count(visit_count)

        moscow_timezone = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_timezone)

        # Separate date and time into two variables
        date_part = current_time.strftime('%Y-%m-%d')
        time_part = current_time.strftime('%H:%M:%S')

        # Render the template with date and time
        return render_template('index.html',
                               date_part=date_part, time_part=time_part)

    except Exception as e:

        # Log the exception (you can also use a logging
        # library for more advanced logging)
        print(f"An unexpected error occurred: {str(e)} ")


        # Return a generic error message to the user
        return f"{str(e)}An unexpected error occurred. " \
               "Please try again later.", 500

@app.route('/visits')
def visits():
    global visit_count
    return f'Total visits: {visit_count}'


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype="text/plain")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
