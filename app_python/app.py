from flask import Flask
from app_utils import return_time, return_index

app = Flask(__name__)


@app.route("/")
def index():
    return return_index()


@app.route("/show")
def show_time():
    return return_time("Europe/Moscow")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
