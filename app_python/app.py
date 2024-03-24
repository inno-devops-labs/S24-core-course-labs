from flask import Flask, render_template, Response
import datetime
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')


@app.route('/')
def index():
    moscow_time = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=3)))
    return render_template('index.html', moscow_time=moscow_time)


if __name__ == "__main__":
    app.run()
