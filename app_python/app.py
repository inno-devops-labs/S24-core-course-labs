from flask import Flask, render_template_string, Response
from datetime import datetime
import pytz
from prometheus_client import Summary, generate_latest

app = Flask(__name__)

REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')


@app.route('/')
@REQUEST_TIME.time()
def index():
    moscow_time = get_moscow_time()
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Moscow Time</title>
    </head>
    <body>
        <h1>The current time in Moscow:</h1>
        <h3>{{ time }}</h3>
    </body>
    </html>
    """
    return render_template_string(html_content, time=moscow_time)


def get_moscow_time():
    moscow = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow)
    return current_time.strftime('%Y-%m-%d %H:%M:%S')


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
