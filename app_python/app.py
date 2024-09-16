"""A Python web application to display the current time in Moscow."""

from datetime import datetime, timezone, timedelta
from flask import Flask, render_template

app = Flask(__name__)


def get_moscow_time():
    """Get the current time in Moscow."""
    moscow_timezone = timezone(timedelta(hours=3))  # Moscow time is UTC+3
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/')
def index():
    """Render the index page with the current time in Moscow."""
    moscow_time = get_moscow_time()
    return render_template('index.html', time=moscow_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
