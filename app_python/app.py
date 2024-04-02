from flask import Flask, render_template
from datetime import datetime
import pytz
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route('/')
def home():
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    return render_template('index.html',
                           time=moscow_time.strftime('%d-%m-%Y %H:%M:%S'))

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
