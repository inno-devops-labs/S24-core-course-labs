# Import necessary modules
from flask import Flask
from datetime import datetime
import pytz
import os

# Create Flask application instance
app = Flask(__name__)


# Define route for homepage
@app.route("/")
def current_time():
    # Get current time in Moscow timezone
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Return response with current time in Moscow
    return f"The current time in Moscow is: {moscow_time}"


# Run the Flask application if script is executed directly
if __name__ == "__main__":
    # Get the port from the environment variable, defaulting to 5000
    port = int(os.environ.get("PORT", 5000))

    # Run the Flask application
    app.run(debug=False, host="0.0.0.0", port=port)
