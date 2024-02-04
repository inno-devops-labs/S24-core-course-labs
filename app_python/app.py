from flask import Flask, render_template

from app_python import time

app = Flask(__name__)


@app.route('/')
def show_time():
    return render_template('time.html', time_in_moscow=time.getMoscowTime('Europe/Moscow'))


if __name__ == '__main__':
    app.run(debug=True)
