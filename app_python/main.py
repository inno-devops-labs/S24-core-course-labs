"""
Current Moscow time app
"""
import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)


@app.route('/')
def display_time():
    """
    Display Moscow time
    """
    moscow = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=current_time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
