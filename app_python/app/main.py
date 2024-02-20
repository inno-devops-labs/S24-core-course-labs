from flask import Flask, render_template

from .time import get_formatted_moscow_time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", moscow_time=get_formatted_moscow_time())
