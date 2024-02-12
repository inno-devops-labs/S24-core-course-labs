from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import pytz

app = Flask(__name__, template_folder='templates', static_folder='../static')

@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        rendered HTML template
    """
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    """
    Get the current time in Moscow timezone and return it as JSON.

    Returns:
        JSON response containing Moscow time
    """
    moscow_time = get_moscow_time()
    return jsonify({'moscow_time': moscow_time})

def get_moscow_time():
    """
    Get the current time in Moscow timezone and format it.

    Returns:
        Formatted string representing the current Moscow time
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_time

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)