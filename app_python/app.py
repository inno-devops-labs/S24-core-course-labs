# Import necessary modules
import os
import pytz
from flask import Flask
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

# Create Flask application instance
app = Flask(__name__)

# Initialize metrics
metrics = PrometheusMetrics(app)

# Define route for homepage
@app.route("/")
def current_time():
    # Get current time in Moscow timezone
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Return response with current time in Moscow
    return f"The current time in Moscow is: {moscow_time}"

@app.errorhandler(404)
def not_found():
    """
    Return error page not found as html
    """
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5001)))