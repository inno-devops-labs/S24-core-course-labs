from flask import Flask
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')


@app.route('/')
def get_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f'The current time in Moscow is: {current_time}'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)
