from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')

def call_time() -> str:
    time_zone = pytz.timezone('Europe/Moscow')
    return datetime.now(time_zone).time().__str__()

if __name__ == '__main__':
    app.run()
    
