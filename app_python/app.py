from flask import Flask, render_template
from datetime import datetime, timezone, timedelta
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route('/')
def index():
    moscow_time = datetime.now(timezone(timedelta(hours=3)))
    return render_template('index.html',
                           time=moscow_time.strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)