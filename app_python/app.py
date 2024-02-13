import pytz
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# global variables
timezone = pytz.timezone('Europe/Moscow')
date_format_string = '%Y-%m-%d %H:%M:%S'

@app.route('/')
def display_current_time():
    current_time = datetime.now(timezone).strftime(date_format_string)
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
