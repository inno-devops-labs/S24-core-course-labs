# app.py

from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask("Moscow_current_time")

# Tell Flask to look for static files in the 'static' folder
app.static_folder = 'static'


@app.route('/')
def index():
    try:
        # Get the current time in Moscow
        moscow_timezone = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_timezone)

        # Separate date and time into two variables
        date_part = current_time.strftime('%Y-%m-%d')
        time_part = current_time.strftime('%H:%M:%S')

        # Render the template with date and time
        return render_template('index.html',
                               date_part=date_part, time_part=time_part)

    except Exception as e:
        # Log the exception (you can also use a logging
        # library for more advanced logging)
        print(f"An unexpected error occurred: {str(e)}")

        # Return a generic error message to the user
        return "An unexpected error occurred. " \
               "Please try again later.", 500


if __name__ == '__main__':
    app.run(debug=True)
