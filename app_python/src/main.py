"""
This application returns Moscow time
"""

from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_time():
    """Get and return Moscow time"""
    date_time = datetime.now(pytz.timezone("Europe/Moscow"))
    return date_time.strftime("%H:%M:%S")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
