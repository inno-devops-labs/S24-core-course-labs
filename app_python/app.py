from flask import Flask, jsonify, Response
from datetime import datetime
from prometheus_client import generate_latest
import pytz

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')


@app.route('/')
def index():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'time_in_moscow': formatted_time})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
