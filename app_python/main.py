"""Web app for showing current time in Moscow"""

from datetime import datetime
from flask import Flask
import pytz


PORT = 5000
app = Flask(__name__)

@app.route('/')
def current_time():
    """Returns current time in Europe/Moscow timezone"""
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    return f"The current time in Moscow is {moscow_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
