from flask import Flask, Response
from datetime import datetime, timezone, timedelta
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route('/')
def show_time():
    moscow_time = datetime.now() + timedelta(hours=3)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
