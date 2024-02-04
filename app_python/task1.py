"""
This is a Python web application that displays the current time in Moscow.
"""
from flask import Flask, render_template
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    """
    Renders the index.html template to display the current time in Moscow.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
