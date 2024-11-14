
from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route('/')
def display_time():
    # Get the current time in Moscow
    moscow_time = datetime.now(timezone(timedelta(hours=3)))

    # Format the time for display
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')

    # Render the template with the formatted time
    return render_template('index.html', time=formatted_time)


if __name__ == '__main__':
    app.run(debug=True)

