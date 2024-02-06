# Import necessary modules
from flask import Flask
from datetime import datetime
import pytz

# Create Flask application instance
app = Flask(__name__)

# Define route for homepage
@app.route('/')
def current_time():
    # Get current time in Moscow timezone
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    
    # Return response with current time in Moscow
    return f'The current time in Moscow is: {moscow_time}'

# Run the Flask application if script is executed directly
if __name__ == '__main__':
    app.run()
