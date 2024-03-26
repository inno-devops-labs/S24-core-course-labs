from flask import Flask, render_template, Response
from datetime import datetime, timezone
import pytz
from prometheus_client import Summary, generate_latest

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


def get_current_time():
    gmt_time = datetime.now(timezone.utc)

    gmt3_timezone = pytz.timezone('Etc/GMT-3')
    gmt3_time = gmt_time.replace(tzinfo=pytz.utc).astimezone(gmt3_timezone)

    return gmt3_time.strftime('%H:%M:%S')


@app.route('/')
@REQUEST_TIME.time()
def index():
    current_time = get_current_time()
    return render_template('index.html', current_time=current_time)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == '__main__':
    app.run(debug=False)
