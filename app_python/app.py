from flask import Flask, render_template, Response
from datetime import datetime, timezone
import pytz
import prometheus_client

app = Flask(__name__)

REQUEST_TIME = prometheus_client.Histogram('py_request_handle_time', 'Time to process a request')


@app.route('/')
@REQUEST_TIME.time()
def display_time():
    moscow_time = get_moscow_time()
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=formatted_time)


def get_moscow_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_utc_time = datetime.utcnow()
    moscow_time = current_utc_time.replace(tzinfo=timezone.utc).\
        astimezone(moscow_timezone)
    return moscow_time

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype="text/plain")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
