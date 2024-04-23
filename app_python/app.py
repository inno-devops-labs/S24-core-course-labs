# Import necessary modules
from flask import Flask
from datetime import datetime
import pytz
import os

# Create Flask application instance
app = Flask(__name__)
visits_file = "visits.txt"


# Function to read visit count from file
def read_visit_count():
    try:
        with open(visits_file, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        # Create the file if it doesn't exist
        with open(visits_file, "w") as file:
            file.write("0")
        return 0


# Initialize visit count
visit_count = read_visit_count()


# Define route for homepage
@app.route("/")
def current_time():
    # Increment visit count
    global visit_count
    visit_count += 1

    # Write visit count to file
    with open(visits_file, "w") as file:
        file.write(str(visit_count))
        
    # Get current time in Moscow timezone
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Return response with current time in Moscow
    return f"The current time in Moscow is: {moscow_time}"


# Define route to display visit count
@app.route("/visits")
def display_visits():
    global visit_count
    return f"Total visits: {visit_count}"


# Run the Flask application if script is executed directly
if __name__ == "__main__":
    # Get the port from the environment variable, defaulting to 5000
    port = int(os.environ.get("PORT", 5000))

    # Run the Flask application
    app.run(debug=False, host="0.0.0.0", port=port)
