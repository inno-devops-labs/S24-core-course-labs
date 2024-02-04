from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    moscow_time = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=3)))
    return render_template('index.html', moscow_time=moscow_time)


if __name__ == "__main__":
    app.run()
