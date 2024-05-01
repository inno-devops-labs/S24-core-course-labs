from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

def get_visits():
    try:
        with open('visits.txt', 'r') as file:
            visits = int(file.read())
        return visits
    except FileNotFoundError:
        with open('visits.txt', 'w') as file:
            file.write('0')
        return 0

def update_visits(visits):
    with open('visits.txt', 'w') as file:
        file.write(str(visits))

@app.route('/')
def get_time():
    try:
        moscow = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')
        visits = get_visits() + 1
        update_visits(visits)
        return f'The current time in Moscow is: {moscow_time}. Visits: {visits}'
    except Exception as e:
        return f'An error occurred: {str(e)}'

@app.route('/visits')
def get_visits_route():
    try:
        visits = get_visits()
        return f'The number of visits is: {visits}'
    except Exception as e:
        return f'An error occurred: {str(e)}'

if __name__ == '__main__':
    app.run()
