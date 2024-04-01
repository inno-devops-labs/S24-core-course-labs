from flask import Flask, Response
from datetime import datetime
import pytz
from prometheus_client import generate_latest


app = Flask(__name__)

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')

@app.route('/')
def call_time() -> str:
    time_zone = pytz.timezone('Europe/Moscow')
    return datetime.now(time_zone).time().__str__()

if __name__ == '__main__':
    app.run()