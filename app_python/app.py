from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def index():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'time_in_moscow': formatted_time})


if __name__ == '__main__':
    app.run()
