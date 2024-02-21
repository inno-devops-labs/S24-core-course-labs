from flask import Flask, render_template

from .utils import get_moscow_time

app = Flask(__name__)


@app.route('/')
def index():
    """Render funtion for start page of the app"""
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
