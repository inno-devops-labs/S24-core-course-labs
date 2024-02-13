from flask import Flask, render_template
from datetime import datetime, timezone, timedelta
import pytz

app = Flask(__name__)


@app.route('/')
def display_time():
    moscow_time = get_moscow_time()
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=formatted_time)


def get_moscow_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_utc_time = datetime.utcnow()
    moscow_time = current_utc_time.replace(tzinfo=timezone.utc).astimezone(moscow_timezone)
    return moscow_time


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
