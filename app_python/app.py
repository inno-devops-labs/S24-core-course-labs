from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def display_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time_moscow = datetime.now(moscow_tz)
    formatted_time = current_time_moscow.strftime('%Y-%m-%d %H:%M:%S %Z')
    return f"Current time in Moscow: {formatted_time}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
