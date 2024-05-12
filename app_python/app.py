from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def get_time():
    try:
        # Get the timezone for Moscow
        moscow = pytz.timezone('Europe/Moscow') 
        
        # Get the current time in Moscow and format it
        moscow_time = datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')
        
        # Return the current time in Moscow as a response
        return f'The current time in Moscow is: {moscow_time}'
    except Exception as e:
        # If an error occurs, return an error message
        return f'An error occurred: {str(e)}'

if __name__ == '__main__':
    app.run()
