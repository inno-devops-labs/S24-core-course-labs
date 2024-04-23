"""Flask web application to display the current time in Moscow."""
import os
from datetime import datetime
from flask import Flask, render_template
import pytz
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)


def read_counter():
    """Read the counter value"""
    if os.path.exists('volume/visits'):
        with open('volume/visits', 'r') as file:
            return int(file.read())
    return 0


def update_counter():
    """Increment the counter"""
    count = read_counter() + 1
    with open('volume/visits', 'w') as file:
        file.write(str(count))
    return count


@app.route('/')
def show_time():
    """Show the current time in Moscow on the homepage."""
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time)


@app.route('/visits')
def show_visits():
    """Display the number of times the app has been accessed."""
    count = read_counter()
    return render_template('visits.html', count=count)


if __name__ == '__main__':
    app.run(debug=True)
