from flask import Flask, Response, jsonify
from datetime import datetime
from pytz import timezone
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route('/')
def show_time():
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    print(moscow_time)
    return jsonify({"time": moscow_time})

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
