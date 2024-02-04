from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
