"""Flask web application to display the current time in Moscow."""

from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    """Show the current time in Moscow on the homepage."""
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time)


if __name__ == '__main__':
    app.run(debug=True)
