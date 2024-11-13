# Import necessary modules
from flask import Flask
from datetime import datetime
import pytz

# Initialize the Flask app
app = Flask(__name__)


# Function to get Moscow time
def get_moscow_time():
    # Get current Moscow time using pytz
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    return moscow_time


# Function to format the time as a string
def format_time(time):
    # Format the datetime object
    return time.strftime('%Y-%m-%d %H:%M:%S')


# Root to see immediately
@app.route('/')
def show_time():
    # Get the Moscow time
    moscow_time = get_moscow_time()

    # Format the Moscow time
    formatted_time = format_time(moscow_time)

    # Return the formatted time in HTML
    return f"<h1>Moscow Time: {formatted_time}</h1>"


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
