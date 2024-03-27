from flask import Flask, Response
from datetime import datetime
from prometheus_client import generate_latest
import pytz

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')

@app.route('/')
def display_time_msk():
    timezone = pytz.timezone('Europe/Moscow')
    time_msk = datetime.now(timezone)
    print("Received request")
    return f"Current time in Moscow: " \
           f"{time_msk.strftime('%Y-%m-%d %H:%M:%S %Z')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
