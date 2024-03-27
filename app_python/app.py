'''
python app - moscow time
'''
import datetime
import pytz
from flask import Flask, render_template, Response
from prometheus_client import generate_latest

app = Flask(__name__)


@app.route('/metrics')
def metrics():
    '''
    metrics
    '''
    return Response(generate_latest(), content_type='text/plain')

# Route for the home page
@app.route('/')
def home():
    '''
    home page 
    '''
    # Get the current time in Moscow
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Render the home.html template with the current time
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
