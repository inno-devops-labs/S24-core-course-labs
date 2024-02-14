from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def display_time_msk():
    timezone = pytz.timezone('Europe/Moscow')
    time_msk = datetime.now(timezone)
    return f"Current time in Moscow: {time_msk.strftime('%Y-%m-%d %H:%M:%S %Z')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)