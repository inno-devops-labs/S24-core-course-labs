from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def template():
    return render_template(
        'index.html', 
        time=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime('%d.%m.%y %H:%M:%S')
    )

if __name__ == '__main__':
    app.run()