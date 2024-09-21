from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route('/')
def show_time():
    moscow_time = datetime.utcnow() + timedelta(hours=3)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
