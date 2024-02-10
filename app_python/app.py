"""
Main application file. Contains the route information and necessary setups.
"""

from flask import Flask
from app_python.app_utils import return_time

app = Flask(__name__)


@app.route("/")
def show_time():
    """
    Index page. Shows the current time in Moscow.
    """
    return return_time("Europe/Moscow")
